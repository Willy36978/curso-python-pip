import matplotlib.pyplot as plt    

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(labels=labels, x=values)
    plt.savfig('pie.png')
    plt.close()
