import matplotlib.pyplot as plt
def go(arg):
    x = [1,2,3,4,5,6]
    y = [5,7,8,8,9,7]

    x2 = [1,2,3,4,5,6]
    y2 = [8,9,12,10,11,13]


    plt.plot(x,y,label='nazis')
    plt.plot(x2,y2,label='aligators')
    plt.xlabel('Years')
    plt.ylabel('Incidents')
    plt.title('The EvidenceProvided\nyesterday')
    plt.legend()
    plt.show()
    print("meh"+arg)
