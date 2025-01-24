from Entities import *
from os import system
from PriorityQueue import PriorityQueue

Rasht = City()


def Add_Pearson(Rasht):
        F_name = input("Enter first name: ")
        L_name = input("Enter last name: ")
        NID = input("Enter NID: ")
        password = input("Enter password: ")
        house_id = input("Enter house ID: ")
        house_location = input("Enter house location: ")
        Rasht.add_people(F_name, L_name, NID, password, house_id, house_location)
        Rasht.add_house(house_id, house_location)
        connected_nodes_entered = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge("M"+house_id, node_id.strip(), int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),"M"+house_id, int(weight))
        return NID, "M" +house_id

while True:
    choice = Rasht.city_menu()
    if choice == "1":
        house_id = input("Enter house ID: ")
        house_location = input("Enter house location: ")
        Rasht.add_house(house_id, house_location)
        connected_nodes_entered = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge("M"+house_id, node_id.strip(), int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),"M"+house_id, int(weight))
        system('clear')
    elif choice == "2":
        hospital_name = input("Enter hospital name: ")
        hospital_id = input("Enter hospital ID: ")
        F_name = input("Enter manager's first name: ")
        L_name = input("Enter manager's last name: ")
        NID = input("Enter manager's NID: ")
        password = input("Enter manager's password: ")
        Rasht.add_hospital(hospital_name, hospital_id, F_name, L_name, NID, password)
        connected_nodes_entered = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge("H"+hospital_id, node_id.strip(), int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),"H"+hospital_id, int(weight))
        system('clear')
    elif choice == "3":
        accesspoint_id = input("Enter access point ID: ")
        accesspoint_location = input("Enter access point location: ")
        Rasht.add_accesspoint(accesspoint_id, accesspoint_location)
        connected_nodes_entered = input("Enter IDs of nodes connected to this access point (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge("A"+accesspoint_id, node_id.strip(), int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this access point (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),"A"+accesspoint_id, int(weight))
        system('clear')
    elif choice == "4":
        ambulance_id = input("Enter ambulance ID: ")
        hospital_id = input("Enter hospital ID: ")
        ambulance_location = input("Enter ambulance location: ")
        new_ambulance = Ambulance(ambulance_id, hospital_id, ambulance_location)
        hospital = Rasht.find_hospital(hospital_id)
        if hospital:
            hospital.Ambulance.append(new_ambulance)
        system('clear')
    elif choice == "5":
        hospital_id = input("Enter hospital ID: ")
        F_name = input("Enter manager's first name: ")
        L_name = input("Enter manager's last name: ")
        NID = input("Enter manager's NID: ")
        password = input("Enter manager's password: ")
        hospital = Rasht.find_hospital(hospital_id)
        if hospital:
            new_manager = HospitalManager(F_name, L_name, NID, password, hospital.hospital_name, hospital_id)
            hospital.Manager = new_manager
        system('clear')
    elif choice == "6":
        F_name = input("Enter first name: ")
        L_name = input("Enter last name: ")
        NID = input("Enter NID: ")
        password = input("Enter password: ")
        house_id = input("Enter house ID: ")
        house_location = input("Enter house location: ")
        Rasht.add_people(F_name, L_name, NID, password, house_id, house_location)
        # Rasht.add_house(house_id, house_location)
        connected_nodes_entered = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge("M"+house_id, node_id.strip(), int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),"M"+house_id, int(weight))
        system('clear')
    elif choice == "7": 
        Rasht.display_city_map()
    elif choice == "8":
        node_id = input("Enter the ID of the node you want to delete: ")
        if "M" in node_id:
            house = Rasht.find_house_by_house_id(node_id)
            citizen = Rasht.finde_citizen_by_NID(house.owner)
            citizen.location = None
        if "H" in node_id:
            hospital = Rasht.find_hospital(node_id)
            current = Rasht.city_ambulances.head
            while current:
                if current.data.Hospital_id == hospital.hospital_id:
                    Rasht.city_ambulances.delete(lambda a: a.Ambulance_id == current.data.Ambulance_id)
                current = current.next
        if "A" in node_id:
            accesspoint = Rasht.find_accesspoint(node_id)
            current = Rasht.city_ambulances.head
            while current:
                if current.data.Ambulance_location == accesspoint.accesspoint_location:
                    current.data.Ambulance_location = current.data.Hospital_id
                current = current.next
        Rasht.delete_node(node_id)
    elif choice == "9":
        hospital_id = input("Enter hospital ID: ")
        password = input("Enter manager's password: ")
        hospital = Rasht.find_hospital(hospital_id)
        if hospital:
            if hospital.Manager.chek_password(password):
                print("Login successful.")
                while True :
                    HM_choice = Rasht.hospital_menu()
                    if HM_choice == "1" :
                        ambulance_id = input("Enter ambulance ID: ")
                        ambulance_location = input("Enter ambulance location: ")
                        hospital.Ambulance.append(Ambulance(ambulance_id, hospital.hospital_id, ambulance_location))
                        Rasht.city_ambulances.append(Ambulance(ambulance_id, hospital.hospital_id, ambulance_location))

                    elif HM_choice == "2":
                        break
            else:
                print("Login failed.")
        else:
            print("Hospital not found.")
    elif choice == "10" or choice == "11":

        if choice == "10":
            NID = input("Enter NID: ")
            password = input("Enter password: ")
            citizen = Rasht.finde_citizen_by_NID(NID)
            if citizen:
                if citizen.chek_password(password):
                    print("Login successful.")
                    house_id = citizen.location.house_id
                    print(f"House ID: {house_id}")
                else:
                    print("Login failed.")
                    continue
                
        else :
            NID, house_id= Add_Pearson(Rasht)

        choose = Rasht.show_hospital()
        if choose != "0":
            hospital_id = Rasht.city_hospitals.get_by_index(int(choose) - 1)
            if hospital_id or house_id:
                Rasht.city_ambulances.display()
                Priority_Q = PriorityQueue()
                current = Rasht.city_ambulances.head
                
                # Store all ambulances with their costs in Priority_Q
                while current != None:
                    path = Rasht.city_graph.a_star_search(current.data.Ambulance_location, house_id)
                    if path:
                        cost = Rasht.city_graph.calculate_path_cost(path)
                        print("Path found:", " -> ".join(path))
                        print("Total path cost:", cost)

                        if current.data.Hospital_id == hospital_id:
                            cost -= 3
                        # Store tuple of (cost, hospital_id, path) in heap
                        Priority_Q.insert((cost, hospital_id, current.data,path))
                    current = current.next

                # Get the minimum cost path from Priority_Q
                if not Priority_Q.is_empty():
                    min_cost, best_hospital, ambulance, best_path = Priority_Q.extract_min()
                    print("\nBest hospital found:")
                    print(f"Hospital: {best_hospital}")
                    print(f"Path: {' -> '.join(best_path)}")
                    print(f"Total cost: {min_cost}")
                    report = Report(best_hospital.hospital_id, ambulance.Ambulance_id, ambulance.Ambulance_location, NID, house_id, min_cost)
                    Rasht.city_reports.put(Report.count, report)
                else:
                    print("No accessible ambulance found.")

    elif choice == "12":
        Rasht.city_reports.display()

    elif choice == "13":
        break
    else:
        print("Invalid choice. Please try again.")