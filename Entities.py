from Hash import Hash
from LinkedList import LinkedList
from Graph import Graph

Hash_agent = Hash()

class City:
    def __init__(self):
        self.city_graph = Graph()
        self.city_emergency_graph = Graph()
        self.city_houses = LinkedList()
        self.city_hospitals = LinkedList()
        self.city_accesspoints = LinkedList()

    def find_house_by_house_id(self, house_id):
        current = self.city_houses.head
        while current:
            if current.data.house_id == house_id:
                return current.data
            current = current.next
        return None

    def find_house_by_owner(self, owner_id):
        current = self.city_houses.head
        while current:
            if current.data.owner == owner_id:
                return current.data
            current = current.next
        return None
    
    def find_hospital(self, hospital_id):
        current = self.city_hospitals.head
        while current:
            if current.data.hospital_id == hospital_id:
                return current.data
            current = current.next
        return None
    
    def find_accesspoint(self, accesspoint_id):
        current = self.city_accesspoints.head
        while current:
            if current.data.accesspoint_id == accesspoint_id:
                return current.data
            current = current.next
        return None
    
    def city_menu(self):
        print("1. Add House")
        print("2. Add Hospital")
        print("3. Add Access Point")
        print("4. Add Ambulance")
        print("5. Add Hospital Manager")
        print("6. Add People")
        print("7. Display city map")
        print("8. Delete a Node from the city map")
        print("9. Exit")
        choice = input("Enter your choice: ")
        return choice
    
    def add_house(self, house_id, house_location):
        new_house = House(house_id, house_location)
        self.city_houses.append(new_house)
        self.city_graph.add_vertex(new_house.house_id, new_house)

    def add_hospital(self, hospital_name, hospital_id, F_name, L_name, NID, password):
        new_manager = HospitalManager(F_name, L_name, NID, password, hospital_name, hospital_id)
        new_hospital = Hospital(hospital_name, hospital_id, new_manager)
        self.city_hospitals.append(new_hospital)
        self.city_graph.add_vertex(hospital_id, new_hospital)

    def add_people(self, F_name, L_name, NID, password, house_id , house_location):
        new_person = People(F_name, L_name, NID, password, house_id , house_location)
        self.city_houses.append(new_person.location)


    def add_accesspoint(self, accesspoint_id, accesspoint_location):
        new_accesspoint = AccessPoint(accesspoint_id, accesspoint_location)
        self.city_accesspoints.append(new_accesspoint)
        self.city_graph.add_vertex(accesspoint_id, new_accesspoint)

    def add_edge(self, vertex1_id, vertex2_id, weight):
        self.city_graph.add_edge(vertex1_id, vertex2_id, weight)
    
    def add_edge_emergency(self, vertex1_id, vertex2_id, weight):
        self.city_emergency_graph.add_edge_emergency(vertex1_id, vertex2_id, weight)
    
    def delete_node(self, node_id):
        self.city_graph.delete_vertex(node_id)
        self.city_houses.delete(lambda h: h.house_id == node_id)
        self.city_hospitals.delete(lambda h: h.hospital_id == node_id)
        self.city_accesspoints.delete(lambda a: a.accesspoint_id == node_id)

    def display_city_map(self):
        self.city_graph.display()

class House:
    def __init__(self, house_id, house_location):
        self.house_id = "M"+ house_id
        self.house_location = house_location
        self.owner = None

    def __str__(self):
        return f"{self.house_id}"
    
class People():
    def __init__(self, F_name, L_name, NID, password, house_id, house_location) :
        self.firstname = F_name
        self.lastname = L_name
        self.__password = self.__set_password(password)
        self.NID = "P"+ NID
        self.location = House(house_id , house_location)
        self.location.owner = self.NID

    def __set_password(self, password):
        self.__password = Hash_agent.update(password)
    
    def get_password(self):
        return self.__password
    
    def __str__(self):
        return f"{self.NID}"

class HospitalManager(People):
    def __init__(self, F_name, L_name, NID, password, hospital_name, hospital_id):
        super().__init__(F_name, L_name, NID, password , hospital_id)
        self.hospital_name = hospital_name
        self.hospital_id = "H"+ hospital_id

        def __str__(self):
            return f"{self.NID}"

class Ambulance:
    def __init__(self, Ambulance_id, hospital_id, Ambulance_location):
        self.Ambulance_id = "C"+  Ambulance_id
        self.Hospital_id = hospital_id
        self.Ambulance_location = Ambulance_location
        self.On_mission = False

    def __str__(self):
            return f"{self.Ambulance_id}"

class Hospital:
    def __init__(self , hospital_name, hospital_id, Manager):
        self.hospital_name = hospital_name
        self.hospital_id = "H"+  hospital_id
        self.Manager = Manager
        self.Ambulance = LinkedList()

class AccessPoint:
    def __init__(self, accesspoint_id, accesspoint_location):
        self.accesspoint_id = "A"+ accesspoint_id
        self.accesspoint_location = accesspoint_location

    def __str__(self):
        return f"{self.accesspoint_id}"

