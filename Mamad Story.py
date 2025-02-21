import random
import time


def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.1)
    print()


def game_intro():
    print_slow("ممد وارد یک خانه متروکه و تاریک می‌شود...")
    print_slow("صدای باد از پنجره‌های شکسته می‌آید. دیوارهای خانه پر از گرد و غبار است...")
    print_slow("ناگهان صدای گام‌های سنگین از طبقه بالا می‌آید. دل ممد می‌لرزد.")
    print_slow("او باید تصمیم بگیرد: آیا بالا برود یا از خانه فرار کند؟")


def choose_action():
    print_slow("1. بالا می‌روی و سراغ صدا می‌ری.")
    print_slow("2. از خانه فرار می‌کنی.")
    
    choice = input("انتخاب خود را وارد کن (1 یا 2): ")
    
    if choice == "1":
        upstairs()
    elif choice == "2":
        escape()
    else:
        print_slow("لطفا یک انتخاب صحیح وارد کن.")
        choose_action()


def upstairs():
    print_slow("\nممد با دلهره به سمت طبقه بالا می‌رود...")
    time.sleep(2)
    print_slow("در تاریکی تنها صدای قدم‌های خودش به گوش می‌رسد.")
    
    if random.randint(1, 2) == 1:
        print_slow("\nناگهان یک سایه از مقابل ممد رد می‌شود! فریاد بلندی به گوش می‌رسد!")
        print_slow("وای! اینجا هیچ کس نیست جز... ممد! او در دنیای تاریک تنهاست!")
        print_slow("ممد در حال دویدن است و قدم‌های سنگین صدای وحشتناکی ایجاد می‌کند.")
        print_slow("فریب خوردی! بازی تمام شد.")
    else:
        print_slow("\nممد به اتاقی قدیمی می‌رسد. در این اتاق هیچ چیز جز اشیای شکسته و گرد و غبار نیست.")
        print_slow("اما یک صندوق چوبی قدیمی در گوشه اتاق توجه ممد را جلب می‌کند.")
        print_slow("آیا ممد جرات می‌کند صندوق را باز کند؟")
        choice = input("1. صندوق را باز می‌کند. 2. از آن دور می‌شود: ")
        
        if choice == "1":
            open_chest()
        elif choice == "2":
            print_slow("\nممد از اتاق خارج می‌شود اما صدای خش خش و نفس‌های عجیب او را به ترس می‌اندازد...")
            print_slow("او تصمیم می‌گیرد از خانه خارج شود. بازی تمام شد.")
        else:
            print_slow("\nانتخاب نامعتبر. بازی تمام شد.")


def open_chest():
    print_slow("\nممد صندوق را باز می‌کند و درون آن یک کتاب قدیمی و یک کلید زنگ زده پیدا می‌کند...")
    print_slow("اما چیزی عجیب و ترسناک در گوشه‌ی اتاق به حرکت در می‌آید!")
    
    if random.randint(1, 2) == 1:
        print_slow("\nناگهان یک دست خون‌آلود از زیر تخت بیرون می‌آید! ممد وحشت‌زده فریاد می‌زند.")
        print_slow("ممد به سرعت از خانه فرار می‌کند.")
        print_slow("بازی تمام شد.")
    else:
        print_slow("\nاما وقتی ممد کتاب را باز می‌کند، ناگهان یک صدای غم‌انگیز در گوشش طنین می‌اندازد...")
        print_slow("این کتاب نفرین شده است!")
        print_slow("ممد در حالی که تلاش می‌کند از خانه بیرون برود، صداهایی مرموز او را تعقیب می‌کنند.")
        print_slow("بازی تمام شد.")


def escape():
    print_slow("\nممد به سرعت از خانه خارج می‌شود...")
    print_slow("در تاریکی خیابان، صدای قدم‌های سنگین هنوز به گوش می‌رسد.")
    print_slow("یک سایه مرموز از پشت پنجره به او خیره شده است...")
    print_slow("ممد از ترس فریاد می‌زند!")
    print_slow("اما هیچکس به کمک او نمی‌آید.")
    print_slow("ممد از ترس در دل شب فرار می‌کند... بازی تمام شد.")


def start_game():
    game_intro()
    choose_action()


start_game()
