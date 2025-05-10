import time
import redis
from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()  
cache = redis.Redis(host=os.getenv('REDIS_HOST'), port=6379,  password=os.getenv('REDIS_PASSWORD'))
app = Flask(__name__)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('hello.html', name= "BIPM", count = count)

@app.route('/titanic')
def titanic():
    import pandas as pd
    import os
    from matplotlib.figure import Figure
    import io
    import base64

    file_path = os.path.join(os.path.dirname(__file__), 'src/titanic.csv')
    df = pd.read_csv(file_path)

    male_survivors = df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]
    female_survivors = df[(df['Sex'] == 'female') & (df['Survived'] == 1)].shape[0]

    fig = Figure()
    ax = fig.subplots()
    ax.bar(['Men', 'Women'], [male_survivors, female_survivors], color=['blue', 'pink'])
    ax.set_title('Survivors by Gender')
    ax.set_ylabel('Count')

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    chart_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    # Pass data to the template
    return render_template(
        'titanic.html',
        survival_data=[male_survivors, female_survivors]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)