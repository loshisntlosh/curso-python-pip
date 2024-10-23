import read_csv
import charts
import utils


def run():
    data= read_csv.read_csv('data.csv')
    data= list(filter(lambda item: item['Continent'] == 'South America', data))
    
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    
    country = input('Type country => ')
    
    result = utils.population_by_country(data, country)

    if len(result) >0:
        country=result[0]    
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)

    '''


    print(result)
    '''


if __name__ == '__main__': #que si es ejecutado en la terminal que ejecute el metodo, y si es desde otro archivo, no es posible
    run()