import os
import re
import pandas as pd

def extract_xyz_from_files(folder_path, line_number, column_indices):
    xyz_array = []
    
    # name Sortieren mit der Nummer
    files = sorted(os.listdir(folder_path), key=lambda x: int(re.findall(r'\d+', x)[-1]))

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # überprüfen ob der line kleiner als die Erlaubnis
            if line_number < len(lines):
                line = lines[line_number].strip()
                
                # Zeile nicht leer
                if line and not line.startswith('#'):
                    columns = line.split()
                    
                    # genug Zeile?
                    if all(i < len(columns) for i in column_indices):
                        # nehmen die bestimmte Postion 
                        x, y, z = [float(columns[i]) for i in column_indices]
                        xyz_array.append((x, y, z))
                    else:
                        print(f"Warning: {filename} does not have enough columns in line {line_number + 1}.")
            else:
                print(f"Warning: {filename} does not have {line_number + 1} lines.")

    return xyz_array
print(extract_xyz_from_files(r"D:\Bauingenieur\studienprojekt\xyz", 3338, [3,4,5]))

xyz_array = extract_xyz_from_files(r"D:\Bauingenieur\studienprojekt\xyz", 3338, [3, 4, 5])
df = pd.DataFrame(xyz_array, columns=["X", "Y", "Z"])
df.to_excel(r"D:\Bauingenieur\studienprojekt\output_xyz.xlsx", index=False)