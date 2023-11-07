import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['1st', '2nd', '3rd']
    values = [220, 140, 90]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

