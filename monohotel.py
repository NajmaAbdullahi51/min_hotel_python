# -- coding: utf-8 --
def get_text(lang):
    data = {
        "en": {
            "main_menu": "\n--- HOTEL MENU ---",
            "options": ["General Info", "Rooms", "Food", "Drinks", "Supermarket", "Change Language", "Exit"],
            "select": "Choose (1-7): ",
            "general_info": "General hotel info:",
            "staff": "Staff:",
            "food_menu": "-- Choose Food --",
            "drinks_menu": "-- Choose Drink --",
            "super_menu": "-- Choose Supermarket Item --",
            "rooms_menu": "-- Choose Room --",
            "thank_you": "Thank you! You chose",
            "lang_changed": "Language changed!",
            "invalid": "Invalid choice, try again.",
            "change_lang": "Select language / اختر اللغة / Dooro luqadda:",
            "langs": ["1. English", "2. Somali", "3. العربية"],
            "total_amount": "Your total amount so far is:"
        },
        "so": {
            "main_menu": "\n--- MENU-GA HOTELKA ---",
            "options": ["Xog guud", "Qolal", "Cunto", "Cabitaan", "Supermarket", "Beddel luqadda", "Ka bax"],
            "select": "Fadlan dooro (1-7): ",
            "general_info": "Xogta guud ee hotelka:",
            "staff": "Shaqaalaha:",
            "food_menu": "-- Door Cunto --",
            "drinks_menu": "-- Door Cabitaan --",
            "super_menu": "-- Door Alaab Supermarket --",
            "rooms_menu": "-- Door Qol --",
            "thank_you": "Mahadsanid! Waad dooratay",
            "lang_changed": "Luqad waa la beddelay!",
            "invalid": "Doorasho khaldan, fadlan isku day mar kale.",
            "change_lang": "Do you want to change language? / Dooro luqad:",
            "langs": ["1. English", "2. Somali", "3. العربية"],
            "total_amount": "Wadarta lacagtaada hadda waa:"
        },
        "ar": {
            "main_menu": "\n--- قائمة الفندق ---",
            "options": ["معلومات عامة", "غرف", "طعام", "مشروبات", "سوبرماركت", "تغيير اللغة", "خروج"],
            "select": "اختر (1-7): ",
            "general_info": "معلومات الفندق العامة:",
            "staff": "الموظفون:",
            "food_menu": "-- اختر الطعام --",
            "drinks_menu": "-- اختر المشروب --",
            "super_menu": "-- اختر غرض من السوبرماركت --",
            "rooms_menu": "-- اختر الغرفة --",
            "thank_you": "شكرًا! لقد اخترت",
            "lang_changed": "تم تغيير اللغة!",
            "invalid": "اختيار غير صالح، حاول مرة أخرى.",
            "change_lang": "اختر اللغة / Select language / Dooro luqadda:",
            "langs": ["1. English", "2. Somali", "3. العربية"],
            "total_amount": "إجمالي المبلغ الخاص بك حتى الآن هو:"
        }
    }
    return data[lang]

# Data
lang = "en"
staff = ["Ayaan", "Cabdi", "Layla"]
food = {"Rice": 3.5, "Pasta": 4.0, "Fish": 5.0, "Bread": 2.0}
drinks = {"Milk": 1.5, "Strawberry Juice": 1.99, "Coca Cola": 1.0, "Lemonade": 1.2}
super_items = {"Oil": 5.0, "Rice 1kg": 1.5, "Sugar 1kg": 1.2, "Tea": 2.0}
rooms = {"Single Room": 20.0, "Double Room": 35.0, "VIP Suite": 70.0}
total = 0  # Wadarta guud

def submenu(menu_dict, menu_title, texts):
    global total
    print(texts[menu_title])
    items = list(menu_dict.items())
    for idx, (it, pr) in enumerate(items, 1):
        print(f"{idx}. {it} = {pr} USD")
    choice = input(texts["select"])
    if not choice.isdigit() or not (1 <= int(choice) <= len(items)):
        print(texts["invalid"])
        return
    it, pr = items[int(choice)-1]
    total += pr
    print(f"\n{texts['thank_you']} {it} = {pr} USD")
    print(f"{texts['total_amount']} {total:.2f} USD\n")

while True:
    t = get_text(lang)
    print(t["main_menu"])
    for i, opt in enumerate(t["options"], 1):
        print(f"{i}. {opt}")
    ch = input(t["select"])

    if ch == "1":
        print(f"\n{t['general_info']}")
        print(f"{t['staff']} {', '.join(staff)}\n")
    elif ch == "2":
        submenu(rooms, "rooms_menu", t)
    elif ch == "3":
        submenu(food, "food_menu", t)
    elif ch == "4":
        submenu(drinks, "drinks_menu", t)
    elif ch == "5":
        submenu(super_items, "super_menu", t)
    elif ch == "6":
        print("\n" + t["change_lang"])
        for opt in t["langs"]:
            print(opt)
        choice = input(t["select"])
        if choice == "1":
            lang = "en"
        elif choice == "2":
            lang = "so"
        elif choice == "3":
            lang = "ar"
        else:
            print(t["invalid"])
            continue
        print("\n" + get_text(lang)["lang_changed"] + "\n")
    elif ch == "7":
        print(f"\n{t['thank_you']} - {t['total_amount']} {total:.2f} USD")
        break
    else:
        print(t["invalid"])


