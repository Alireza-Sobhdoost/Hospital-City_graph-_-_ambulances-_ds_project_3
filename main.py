from Entities import *
from os import system

Rasht = City()

while True:
    choice = Rasht.city_menu()
    if choice == "1":
        house_id = input("Enter house ID: ")
        house_location = input("Enter house location: ")
        Rasht.add_house(house_id, house_location)
        # connected_nodes = input("Enter IDs of nodes connected to this house (comma-separated): ").split(',')
        # for node in connected_nodes:
        #     node_id, weight = node.split(':')
        #     Rasht.add_edge_emergency(house_id, node_id.strip(), int(weight))
        connected_nodes_entered = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),house_id, int(weight))

        connected_nodes_exited = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(house_id, node_id.strip(), int(weight))

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
                Rasht.add_edge(node_id.strip(),hospital_id, int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(hospital_id, node_id.strip(), int(weight))

        system('clear')
        
    elif choice == "3":
        accesspoint_id = input("Enter access point ID: ")
        accesspoint_location = input("Enter access point location: ")
        Rasht.add_accesspoint(accesspoint_id, accesspoint_location)
        # connected_nodes = input("Enter IDs of nodes connected to this access point (comma-separated): ").split(',')
        # for node in connected_nodes:
        #     node_id, weight = node.split(':')
        #     Rasht.add_edge(accesspoint_id, node_id.strip(), int(weight))
        connected_nodes_entered = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_entered != ['']:
            for node in connected_nodes_entered:
                node_id, weight = node.split(':')
                Rasht.add_edge(node_id.strip(),accesspoint_id, int(weight))
        connected_nodes_exited = input("Enter IDs of nodes connected to this hospital (comma-separated): ").split(',')
        if connected_nodes_exited != ['']:
            for node in connected_nodes_exited:
                node_id, weight = node.split(':')
                Rasht.add_edge(accesspoint_id, node_id.strip(), int(weight))

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
        system('clear')
    
    elif choice == "7": 
        Rasht.display_city_map()
    elif choice == "8":
        node_id = input("Enter the ID of the node you want to delete: ")
        Rasht.delete_node(node_id)
    elif choice == "9":
        break
    else:
        print("Invalid choice. Please try again.")