import Client
import Application


def print_order(line):
    print(line + "\nPlease enter your order : ", end='')

def check_range(first, second, third):
    if first >= 0 and first <= 5 and second >= 0 and second <= 5 and third >= 0 and third <= 5:
        return True
    return False

if __name__ == '__main__':
    print("Welcome to Second Phase !")
    while True:
        print_order("1- Sign In 2- Sign Up")
        order = int(input())
        if order == 1:
            while True:
                print("========= Sign In ==========")
                username = input("Username : ")
                password = input("Password : ")
                if Client.signing_checker(username, password) is True:
                    chosen_client = Client.client_getter(username, password)
                    while True:
                        print("========= Market ===========")
                        print_order("1- All Applications 2- Create New Application\n3- All Users 4- Account 5- Pass To First")
                        order = int(input())
                        if order == 1:
                            if len(Application.ApplicationClass.applications_list) > 0:
                                counter = 0
                                for each_app in Application.ApplicationClass.applications_list.display():
                                    print("======================", counter + 1, "========================")
                                    print(each_app.app_name, "@" + each_app.programmer_name)
                                    print("Downloaded", each_app.downloaded_times, "times.")
                                    print("Strategy :", ("*" * int(each_app.strategy_rate)) if each_app.strategy_rate is not None else ("N/A"))
                                    print("Sports :", ("*" * int(each_app.sports_rate)) if each_app.sports_rate is not None else ("N/A"))
                                    print("Simulation :", ("*" * int(each_app.simulation_rate)) if each_app.simulation_rate is not None else ("N/A"))
                                    counter += 1
                                order = int(input("Please choose an app : "))
                                order -= 1
                                if order >= 0 and order <= len(Application.ApplicationClass.applications_list):
                                    while True:
                                        chosen_app = Application.ApplicationClass.applications_list.display()[order]
                                        print("======================", chosen_app.app_name, "========================")
                                        print()
                                        print("By @" + chosen_app.programmer_name)
                                        print("Downloaded", chosen_app.downloaded_times, "times.")
                                        print()
                                        print("Strategy :", ("*" * int(chosen_app.strategy_rate)) if chosen_app.strategy_rate is not None else ("N/A"))
                                        print("Sports :", ("*" * int(chosen_app.sports_rate)) if chosen_app.sports_rate is not None else ("N/A"))
                                        print("Simulation :", ("*" * int(chosen_app.simulation_rate)) if chosen_app.simulation_rate is not None else ("N/A"))
                                        print()
                                        print_order("1- Download 2- Rate 3- Recommended Applications 4- Back")
                                        action = int(input())
                                        if action == 1:
                                            chosen_app.downloaded_times += 1
                                            if chosen_client.downloaded_apps.is_in_list(chosen_app) is False:
                                                chosen_client.downloaded_apps.append(chosen_app)
                                        elif action == 2:
                                            given_strategy_rate = int(input("Strategy Rate (0 to 5): "))
                                            given_sports_rate = int(input("Sports Rate (0 to 5): "))
                                            given_simulation_rate = int(input("Simulation Rate (0 to 5): "))
                                            if check_range(given_strategy_rate, given_sports_rate, given_simulation_rate) is True:
                                                chosen_app.add_strategy_rate(given_strategy_rate)
                                                chosen_app.add_sports_rate(given_sports_rate)
                                                chosen_app.add_simulation_rate(given_simulation_rate)
                                                print("Rated !")
                                        elif action == 3:
                                            recoms = Application.get_recommendations(chosen_app)
                                            name_counter = 1
                                            for each in recoms:
                                                print(str(name_counter) + "-", each)
                                                name_counter += 1
                                        elif action == 4:
                                            break
                            else:
                                print("NO APPS FOUND !")
                        elif order == 2:
                            app_name = input("Application Name : ")
                            dev_name = input("Developed By : ")
                            if Application.app_adder(app_name.strip()) is True:
                                new_app = Application.ApplicationClass(app_name, dev_name)
                                Application.ApplicationClass.applications_list.append(new_app)
                            else:
                                print("Application Name Already Exists !")
                        elif order == 3:
                            print("==============================================")
                            for each_client in Client.ClientClass.clients_list.display():
                                print("@" + each_client.username)
                            print("==============================================")
                        elif order == 4:
                            print("==============================================")
                            print("You have signed in as", "@" + username)
                            dl_line = ""
                            for each_app in chosen_client.downloaded_apps.display():
                                dl_line += " " + each_app.app_name
                            print("Downloaded Applications :", dl_line[1:])
                            print("==============================================")
                        elif order == 5:
                            Application.pass_first_to_second()
                else:
                    print("Wrong username or password !")
        elif order == 2:
            while True:
                print("========= Sign In ==========")
                username = input("Username : ")
                password = input("Password : ")
                if username.strip() != "" and password.strip() != "":
                    new_client = Client.ClientClass(username, password)
                    Client.ClientClass.clients_list.append(new_client)
                    break