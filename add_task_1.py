def remove_duplicates(tickets):
    temp = []
    for priority in tickets.keys():
        unique_tickets = []
        for ticket in tickets[priority]:
            if ticket not in temp:
                unique_tickets.append(ticket)
                temp.append(ticket)
        tickets[priority] = unique_tickets
    return tickets

def tickets_by_type(types, tickets):
    tickets_by_type = {}
    for key in types.keys():
        if key in tickets:
            tickets_by_type[types[key]] = tickets[key]
    return tickets_by_type
        
    

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
    
}


tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

remove_duplicates(tickets)
print(tickets_by_type(types, tickets))
