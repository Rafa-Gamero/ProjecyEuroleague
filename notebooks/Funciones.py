import pandas as pd

# Cargar los datos
df = pd.read_csv('C:/Users/Casa/Documents/GitHub/ProyectoFinal/data cleaned/box_score_2023.csv')

# Convertir minutos de formato MM:SS a número decimal
def convertir_minutos_a_decimal(minutos):
    if minutos == 'DNP':
        return None  # O usa 0 si prefieres
    mins, secs = map(int, minutos.split(':'))
    return mins + secs / 60

df['minutes_decimal'] = df['minutes'].apply(convertir_minutos_a_decimal)


df['minutes_decimal'] = df['minutes'].apply(convertir_minutos_a_decimal)

# Calcular posesiones aproximadas para cada jugador
df['possessions'] = df['two_points_attempted'] + df['three_points_attempted'] + 0.44 * df['free_throws_attempted'] - df['offensive_rebounds'] + df['turnovers']

# Calcular eficiencia ofensiva (puntos anotados por posesión)
df['offensive_efficiency'] = df['points'] / df['possessions']

# Eficiencia defensiva: puntos permitidos por posesión del oponente (aproximación simple)
# En este caso, como no tenemos datos del equipo contrario, lo dejamos como eficiencia inversa del rendimiento del jugador
df['defensive_efficiency'] = 1 / df['offensive_efficiency']

# Visualizar los primeros registros con las nuevas columnas
print(df[['player', 'points', 'possessions', 'offensive_efficiency', 'defensive_efficiency']].head())

# Guardar el nuevo archivo con las métricas calculadas
df.to_csv('euroleague_players_efficiency.csv', index=False)
