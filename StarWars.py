import random

print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣶⡿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⢶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢶⡤⠶⠶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠖⠛⠋⠉⢉⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢦⣄⣤⡤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⠾⠏⠁⠀⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡍⠙⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠉⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣤⣤⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢤⠀⠀⠀⠀⠀⠀⠀⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠛⠶⣤⣄⠀⠀⠀⠀⠀⣠⣠⣤⣤⣤⣴⣶⠶⠿⠛⢛⠒⠋⣿⡇⠀⠀⠀⠀⣠⣴⣶⣶⣶⣦⣄⠀⠀⠑⣄⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⢿⣦⣤⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠿⣦⡀⠀⠀⠀⠙⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⢀⣾⣿⡟⠉⠈⣿⣿⣿⣿⣄⠀⠈⠀⠀⠀⠀⠀⠉⠃⠀⠀⠀⢀⠔⠋⠀⠀⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠷⣤⣄⣀⠀
⠀⠀⠀⠀⠀⠀⠉⢿⣶⡀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⢠⣼⡿⠉⠀⠀⢸⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠁⠀⢀⣤⣶⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠻⢶⣤⣐⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣽⡿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣶⣄⠀⠀⠀⠙⠢⣄⡀⠀⠀⣸⣿⠀⠀⢰⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢀⠶⠀⠀⠀⠀⠀⣴⣿⡋⠀⢨⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠉⠉⠈⠛⠳⠦⠦⢤⣄⣤⠀⠀⠀⠀⠀⢠⣾⠟⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⣷⣤⣀⣀⣀⣀⣉⠙⠒⢿⣿⠀⠀⠈⠻⠏⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠂⠀⠀⠀⢸⡿⣿⡖⠀⠀⠀⣾⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⡏⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡠⠞⠛⠁⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠳⣦⣜⣿⣯⣀⡀⢀⡀⡀⠉⠛⢿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⣨⡀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢀⣠⣤⠶⠛⠁⠀⠀⣀⣀⣀⣤⣴⠶⠛⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢏⠩⣽⠛⠿⠿⣶⣤⣀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠉⣜⡣⠀⣠⡤⠀⠀⠀⠉⠡⠖⠛⠉⠀⠀⢀⣤⣾⣿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣮⣧⡬⢄⢲⣈⣖⡘⠻⢿⣶⣦⡶⡦⣴⣶⣶⣾⣿⣿⣿⣿⡿⣿⣶⣶⣤⣀⠀⠀⠈⠉⠛⠛⠛⣻⣽⣧⠦⡴⠦⠾⡷⣶⣿⣭⣄⣀⣀⢀⣀⢀⠀⡀⣀⣠⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⠟⢿⣶⡰⣿⣷⡿⣿⣖⣻⣽⣷⣷⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠶⣤⣤⣶⠟⣫⠁⡀⢂⠐⠨⠐⢂⠁⠌⠀⡿⢻⢿⣟⠉⠉⠛⠛⠙⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠿⠓⠀⢂⠐⠋⡑⢻⢽⣿⣿⣿⣿⠁⢲⡿⢻⣼⠛⡟⢫⢋⠟⣋⠯⠿⢿⣿⣿⣩⠙⢷⣦⣈⠙⠻⠯⣷⣖⠾⠦⣵⣌⡄⣈⠂⠡⠌⢉⠠⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⡃⠠⢁⠂⢈⢰⣴⡿⠟⢫⣿⠃⠻⣇⠀⢀⣟⣿⣗⡸⡡⢞⡼⣔⢯⡱⡞⣿⣟⠛⠃⢸⡏⠛⣷⣤⡌⠁⠹⣟⢳⠶⠿⣿⠇⢁⠂⠌⢂⠈⢹⣿⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢃⡆⢁⠂⡈⣖⣾⢛⠁⢈⣿⡏⠀⠀⠙⠛⣻⣿⣟⠳⢿⣷⣧⣶⣬⣾⣶⣿⢿⣟⣃⣴⡿⠁⠀⠘⣿⡄⠀⣀⣽⡖⢉⠠⢈⠀⢂⢈⠐⠤⣬⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣠⡁⠂⠌⡀⣾⣯⠘⠀⠀⠻⣷⣤⣀⣠⣴⣿⣿⠉⢋⡇⠓⠘⢷⡻⡶⢀⢿⠀⢹⣯⡁⠀⠀⠀⣰⡿⡁⠀⠈⠘⣿⣂⡐⠠⢁⠂⢌⠀⠚⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣴⠀⠡⠂⠄⢹⡹⣷⣤⠄⠀⠈⠉⡙⢩⣼⡿⠀⣼⣟⠆⡈⠐⡈⣇⣷⡈⢼⡄⢀⠙⠿⠶⢶⡾⠛⠁⠀⠀⠀⠀⣿⣷⡄⠡⠂⠌⠠⢈⠰⣻⣿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣾⡅⠐⡈⠄⢣⣐⠙⢷⢾⣦⠴⠟⠛⠉⢀⣽⣿⡿⢀⣼⢡⠐⡁⣿⣇⣼⠳⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢻⣷⠁⠌⡠⡱⣶⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣵⡦⡌⠠⢈⠉⠲⢬⣀⣄⣀⣀⣤⣿⣿⠏⠐⣧⡿⡯⢀⠐⢲⣿⡜⣾⣿⣦⣄⡀⠀⠀⢀⣠⡤⠞⢋⣽⠀⢛⣿⣿⣶⣾⣿⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⡿⣿⣷⣒⠀⢊⣷⣖⣂⣍⣩⣍⣿⡿⠡⢀⡾⣿⣷⡰⠀⡈⠃⢸⣿⠀⢙⠻⢿⣿⣟⣋⣉⣡⣀⣭⣶⣿⠀⣱⣿⢻⣿⣁⠠⢽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡏⢻⡷⠉⠻⢿⣿⣶⣷⣾⠿⢟⠋⡉⠡⠁⡐⠠⢰⣿⣇⠱⢀⠐⡈⠐⣹⡇⡄⢂⠠⠙⢹⣿⣻⣛⡿⠿⠿⣿⡿⠿⠋⠄⠻⠃⠄⠛⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠉⠄⠠⠐⠠⢁⠠⠁⡼⡟⠁⡐⢈⠐⠠⢁⠂⠄⠡⣾⢿⣧⡁⢂⠰⢀⠡⠀⣿⠡⢀⠂⠌⠠⡸⣷⡭⡁⠄⡘⠀⠄⡀⢂⠌⠠⠁⠌⡀⢻⣿⣇⡀⠄⠀⣀⡀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣪⢀⠡⠌⡐⢀⠢⢵⡞⠱⢀⠰⠀⠌⡐⠠⠌⠠⣵⣿⣸⡷⠞⠀⡐⠠⢂⠁⢾⣧⡂⠌⠠⢁⠐⠚⣿⣧⣐⠠⢁⠂⡐⢀⠂⠁⠌⡐⠠⢁⠩⢿⣿⠄⣀⣉⢀⡀⠁⢠⠀⠀⢀⠀⠄⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠻⢾⣴⣦⣰⣄⣼⢿⠓⢀⠂⠄⢃⠐⠠⠑⠨⢠⣿⣿⣿⢓⠀⢂⠐⠡⠂⡈⢤⢻⡼⡄⢁⠂⡌⠐⠘⣿⣾⠀⠄⠒⠐⠠⢈⠐⣀⢆⣡⣭⣾⣿⡋⣜⣝⠋⠘⠣⠀⠠⠴⠠⠔⠰⠤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠋⡈⢤⡤⠄⢲⣔⣤⣬⠭⣭⣿⠟⡿⣿⣧⣴⣈⣄⣈⢡⣉⠒⣃⣷⣾⣿⠿⠿⢿⣶⣿⣖⡖⡈⠄⡁⠄⢂⠒⡈⠤⠁⠄⠿⣿⣣⣀⠁⣂⣣⣶⣾⣿⣛⡛⠝⡶⠬⠷⠶⠀⠿⠃⠡⠿⠏⠉⠉⠙⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⡀⠈⠁⣩⣿⡋⠙⢛⡋⢛⡋⡍⠙⠋⠛⠛⠛⠚⠛⠿⠟⢷⣤⡶⣦⣬⣿⣷⣿⣵⣒⣈⡀⢡⣐⣀⣤⣉⣹⣋⣿⣶⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠛⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠁⠀⠀⠀⠀⠈⠁⠈⠉⠉⠉⠉⠉⠛⠛⠛⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                           Try not.
                           Do or do not.
                           There is no try.
                            
                                   -Yoda
""")

print('Welcome to Star Wars Adenture Game!' )
jedi_name=input('Enter your name of Jedi Knight : ')
Jediname = jedi_name.title()
print('Hello,',Jediname,'you have to stand against black holes and enemies.')
print('Your mission is to restore peace to the galaxy.' + '\n')
    
score = 0
credit = 0
health = 100
planets = ["Tatooine", "Endor", "Hoth", "Coruscant"]
enemy_health = random.randint(50,100)
while health > 0 and credit < 100 :
    print('\nYour score : ', score) 
    print('Your health : ', health)
    print('Your credit : ', credit)
        
    planet = random.choice(planets)
    print('You are now on the planet', planet)
    choice = input('Do you want to (1) explore the planet or (2) engage in a space battle? (Enter 1 or 2): ')

    if choice == '1':
        credit += random.randint(1, 10)
        print('You explore',planet,' and found',credit ,'credits. ')
    elif choice == '2':
        print('prepare for a space battle with the Empire! Enemy\'s health: ', enemy_health )
    
    while enemy_health > 10 and health > 0:
          player_damage = random.randint(10, 20)
          enemy_damage = random.randint(0,15)
          health -= enemy_damage
          enemy_health -= player_damage
          print('you attacked, dealing', player_damage, 'damage. your health: ', health)
          print('the enemy attacked, dealing', enemy_damage, 'damage. enemy health: ', enemy_health)
             # Enemy attack you

    else:
        print(' :( ')
            
    print('\nYour credit : ', credit)
    print('Your score : ', score) 
    print('Your health : ', health)
    print('Choose one of the options :')
    print('1) Attack')
    print('2) protection')
    print('3) Collection of weapons')
    print('4) Exit')

    Choice = input('Enter (1-4) your choice : ')

    if Choice == '1' :
        damage = random.randint(10, 30)
        print('You attacked and dealt damage to an enemy!', '+', damage)
        score += damage
            # attack the enemy
        
    elif Choice == '2' :
        defence = random.randint(5, 15)
        print('You defended yourself and preserved your health!')
        health += defence
            # defence

    elif Choice == '3' :
        weapon = random.choice(['Lightsaber', 'Blaster', 'Force Push', 'Autoturret', 'AB-75 Bo-rifle', 'anakin skywalker\'s second lightsaber'])
        print('You found a new weapon! : ' + weapon , '+20')
        score += 20
            # weapon

    elif Choice == '4' :
        print('Thanks for playing! Your final score :', score )
        break
            # exit

    else:
        print('Choose a valid option!')
            
    enemyAttack = random.randint(0,15)
    print('the enemy attacked, dealing', enemyAttack, 'damage.')
    health -= enemyAttack

    if health <= 0:
       print('Unfortunately, you failed! Your final score :',score)
