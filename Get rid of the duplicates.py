student_data = {'id1':
    {'name': ['Sara'],
     'class': ['V'],
     'subject_integration': ['English, Math, Science']    
     },
     'id2':
    {'name': ['David'],
     'class': ['V'],
     'subject_integration': ['English, Math, Science']    
     },
     'id3':
    {'name': ['Sara'],
     'class': ['V'],
     'subject_integration': ['English, Math, Science']    
     },
     'id4':
    {'name': ['Surya'],
     'class': ['V'],
     'subject_integration': ['English, Math, Science']    
     },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)