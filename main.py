import sys
    
print(f"Liczba argumentów: {len(sys.argv)}")

for i, arg in enumerate(sys.argv):
    print(f"argument {i:>6}: {arg}")

    if arg == "-help":
        print("Aby uruchumić wpisz w terminalu: 'python main.py -run <ścieżka do pliku config> <ściezka do pliku z danymi>'")

    if arg == "-run":
        try:
            config_path = sys.argv[i+1]
        except(IndexError):
            print('brak ściezki config')
        
        try:
            data_path = sys.argv[i+2]
        except(IndexError):
            print('brak ściezki danych')
