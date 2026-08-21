# Chinese Zodiac
## Code and output
##Name: Zuleyka Clio Arcilla
##Section: Beryllium
##Date Accomplished: August 21, 2026

birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid year. You are too old to be in this program.")
else:
    zodiac_index = (birth_year - 1900) % 12

    if zodiac_index == 0:
        print("Your chinese zodiac is Rat (鼠 / Shǔ).")
    elif zodiac_index == 1:
        print("Your chinese zodiac is Ox (牛 / Niú).")
    elif zodiac_index == 2:
        print("Your chinese zodiac is Tiger (虎 / Hǔ).")
    elif zodiac_index == 3:
        print("Your chinese zodiac is Rabbit (兔 / Tù).")
    elif zodiac_index == 4:
        print("Your chinese zodiac is Dragon (龙 / Lóng).")
    elif zodiac_index == 5:
        print("Your chinese zodiac is Snake (蛇 / Shé).")
    elif zodiac_index == 6:
        print("Your chinese zodiac is Horse (马 / Mǎ).")
    elif zodiac_index == 7:
        print("Your chinese zodiac is Goat (羊 / Yáng).")
    elif zodiac_index == 8:
        print("Your chinese zodiac is Monkey (猴 / Hóu).")
    elif zodiac_index == 9:
        print("Your chinese zodiac is Rooster (鸡 / Jī).")
    elif zodiac_index == 10:
        print("Your chinese zodiac is Dog (狗 / Gǒu).")
    elif zodiac_index == 11:
        print("Your chinese zodiac is Pig (猪 / Zhū).")
        
<img width="1094" height="211" alt="Screenshot 2026-08-21 055510" src="https://github.com/user-attachments/assets/7c50253d-b355-4e78-be8b-e1e6ce88d408" />
