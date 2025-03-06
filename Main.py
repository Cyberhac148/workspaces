

#level one
def get_free_tables(tables):
    free_tables = []
    index = 0
    while index <len(tables):
        table = tables[index]
        if table["occupied"] == False:
            free_tables.append(table["table_id"])
        index +=1
return free_tables

def find_one_table(tables, party_size):
    index = 0
    while index < len(tables):
        table = tables[index]
        if table ["occupied"] == False and table["capacity"] >= party_size:
            return table["table_id"]
        index +=1
    return None

def find_all_tables(tables, party_size):
    available_tables = []
    index = 0
    while index < len(tables):
        table = tables[index]
        if table ["capacity"]>= party_size:
            available_tables.append(table["table_id"])
        index += 1
    return available_tables

def find_table_combos(tables, party_size):
    combos = []
    index = 0
    while index < len(tables):
        table = tables[index]
        if table['occupied'] == False and table["capacity"] >= party_size:
            combos.append(table["table_id"])

        if table["neighbors"]:
            neighbor_index = 0
            while neighbor_index < len(table["neighbors"]):
                neighbor_id = table["neighbors"][neighbor_index]
                neighbor_table = None
                neighbor_table_index = 0
                
                while neighbor_table_index <len(tables):
                    if tables[neighbor_tables_index]["table_id"] == neighbor_id:
                        neighbor_table = tables[neighbor_table_index]
                        break
                    neighbor_table_index += 1
                
                if neighbor_table and neighbor_table["occupied"] == False:
                    total_capacity = table["capacity"] + neighbor_table["capacity"]
                    if total_capacity >= party_size:
                        combos = tupe(soreted([table["table_id"], neighbor_table["table_id"]]))
                        combos.append(combo)

                    neighbor_index += 1
                index += 1
            return possible_combos
        





tables_data =[
    {"table_id": 1, "capacity": 2, "occupied": False},
    {"table_id": 2, "capacity": 4, "occupied": True},
    {"table_id": 3, "capacity": 2, "occupied": False},
    {"table_id": 4, "capacity": 6, "occupied": False}
]