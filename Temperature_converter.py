    

def cToFconverter():
    while True:
        cTemp = input("Please enter C Degree ")

        if cTemp:
            cTemp=float(cTemp) #str to float
            fTemp = 9*cTemp/5 + 32
            print(f"{cTemp}C is converted to {fTemp}F")
            break
    
        else:
            print("cTemp input is empty")
            continue

def main():
    cToFconverter()
if __name__ == "__main__":
    main()