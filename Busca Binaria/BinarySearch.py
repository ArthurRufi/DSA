occupied_apartment = [101, 103, 104, 106, 201, 202, 204,
                    205, 206, 207, 212, 215, 216, 217, 301, 302, 303, 304, 305,
                    306, 307, 308, 309, 310, 311, 312, 313, 314, 315,
                    816, 817, 818, 819, 820, 821, 822, 823, 824, 825,
                    826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836,
                    837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847,
                    848, 849, 850, 851, 852, 853, 854, 855, 856, 857,
                    858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868,
                    869, 870, 871, 872, 873, 874, 875, 877, 878, 879, 880,
                    881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 892, 893, 894, 895, 896, 897, 
                    898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911,
                    912, 913, 914, 915, 916, 917, 918]

def binarySearch(lista, valorProcurado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        numeroMeio = (inicio + fim) // 2

        if lista[numeroMeio] == valorProcurado:
            return numeroMeio
        
        if lista[numeroMeio] < valorProcurado:
            inicio = numeroMeio + 1
        else:
            fim = numeroMeio - 1

    return -1

myTarget = 315

result = binarySearch(occupied_apartment, myTarget)

if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")