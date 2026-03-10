import matplotlib.pyplot as plt

def generate_chart(income, debt):

    labels = ["Income", "Debt"]
    values = [income, debt]

    plt.figure()
    plt.bar(labels, values)

    plt.title("Financial Overview")

    path = "static/chart.png"

    plt.savefig(path)

    return path