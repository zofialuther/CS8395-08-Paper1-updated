from datetime import datetime

def main():
    millis = int(datetime.now().timestamp() * 1000)
    print(datetime.utcfromtimestamp(millis/1000).strftime('%Y-%m-%d'))
    print(datetime.utcfromtimestamp(millis/1000).strftime('%A, %B %d, %Y'))

if __name__ == "__main__":
    main()