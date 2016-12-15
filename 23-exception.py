while True:
    try:
        fish=int(input("what's your number?\n"))
        print(18/fish)
        break
    except ValueError:
        print("type correct one")
    except ZeroDivisionError:
        print("what the hack")
    except:
        print("f**k u")
        break
    finally:
        print("loop complete")