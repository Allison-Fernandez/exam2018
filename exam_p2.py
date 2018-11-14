year_file = {1880:'babynames\yob1880.txt', 1881:'babynames\yob1881.txt', 1882:'babynames\yob1882.txt', 1883:'babynames\yob1883.txt', 1884:'babynames\yob1884.txt', 1885:'babynames\yob1885.txt', 1886:'babynames\yob1886.txt', 1887:'babynames\yob1887.txt', 1888:'babynames\yob1888.txt', 
1889:'babynames\yob1889.txt', 1890:'babynames\yob1890.txt', 1891:'babynames\yob1891.txt', 1892:'babynames\yob1892.txt', 1893:'babynames\yob1893.txt', 1894:'babynames\yob1894.txt', 1895:'babynames\yob1895.txt', 1896:'babynames\yob1896.txt', 1897:'babynames\yob1897.txt', 1898:'babynames\yob1898.txt', 
1899:'babynames\yob1899.txt', 1900:'babynames\yob1900.txt', 1901:'babynames\yob1901.txt', 1902:'babynames\yob1902.txt', 1903:'babynames\yob1903.txt', 1904:'babynames\yob1904.txt', 1905:'babynames\yob1905.txt', 1906:'babynames\yob1906.txt', 1907:'babynames\yob1907.txt', 1908:'babynames\yob1908.txt', 
1909:'babynames\yob1909.txt', 1910:'babynames\yob1910.txt', 1911:'babynames\yob1911.txt', 1912:'babynames\yob1912.txt', 1913:'babynames\yob1913.txt', 1914:'babynames\yob1914.txt', 1915:'babynames\yob1915.txt', 1916:'babynames\yob1916.txt', 1917:'babynames\yob1917.txt', 1918:'babynames\yob1918.txt', 
1919:'babynames\yob1919.txt', 1920:'babynames\yob1920.txt', 1921:'babynames\yob1921.txt', 1922:'babynames\yob1922.txt', 1923:'babynames\yob1923.txt', 1924:'babynames\yob1924.txt', 1925:'babynames\yob1925.txt', 1926:'babynames\yob1926.txt', 1927:'babynames\yob1927.txt', 1928:'babynames\yob1928.txt', 
1929:'babynames\yob1929.txt', 1930:'babynames\yob1930.txt', 1931:'babynames\yob1931.txt', 1932:'babynames\yob1932.txt', 1933:'babynames\yob1933.txt', 1934:'babynames\yob1934.txt', 1935:'babynames\yob1935.txt', 1936:'babynames\yob1936.txt', 1937:'babynames\yob1937.txt', 1938:'babynames\yob1938.txt',
1939:'babynames\yob1939.txt', 1940:'babynames\yob1940.txt', 1941:'babynames\yob1941.txt', 1942:'babynames\yob1942.txt', 1943:'babynames\yob1943.txt', 1944:'babynames\yob1944.txt', 1945:'babynames\yob1945.txt', 1946:'babynames\yob1946.txt', 1947:'babynames\yob1947.txt', 1948:'babynames\yob1948.txt', 
1949:'babynames\yob1949.txt', 1950:'babynames\yob1950.txt', 1951:'babynames\yob1951.txt', 1952:'babynames\yob1952.txt', 1953:'babynames\yob1953.txt', 1954:'babynames\yob1954.txt', 1955:'babynames\yob1955.txt', 1956:'babynames\yob1956.txt', 1957:'babynames\yob1957.txt', 1958:'babynames\yob1958.txt', 
1959:'babynames\yob1959.txt', 1960:'babynames\yob1960.txt', 1961:'babynames\yob1961.txt', 1962:'babynames\yob1962.txt', 1963:'babynames\yob1963.txt', 1964:'babynames\yob1964.txt', 1965:'babynames\yob1965.txt', 1966:'babynames\yob1966.txt', 1967:'babynames\yob1967.txt', 1968:'babynames\yob1968.txt', 
1969:'babynames\yob1969.txt', 1970:'babynames\yob1970.txt', 1971:'babynames\yob1971.txt', 1972:'babynames\yob1972.txt', 1973:'babynames\yob1973.txt', 1974:'babynames\yob1974.txt', 1975:'babynames\yob1975.txt', 1976:'babynames\yob1976.txt', 1977:'babynames\yob1977.txt', 1978:'babynames\yob1978.txt', 
1979:'babynames\yob1979.txt', 1980:'babynames\yob1980.txt', 1981:'babynames\yob1981.txt', 1982:'babynames\yob1982.txt', 1983:'babynames\yob1983.txt', 1984:'babynames\yob1984.txt', 1985:'babynames\yob1985.txt', 1986:'babynames\yob1986.txt', 1987:'babynames\yob1987.txt', 1988:'babynames\yob1988.txt', 
1989:'babynames\yob1989.txt', 1990:'babynames\yob1990.txt', 1991:'babynames\yob1991.txt', 1992:'babynames\yob1992.txt', 1993:'babynames\yob1993.txt', 1994:'babynames\yob1994.txt', 1995:'babynames\yob1995.txt', 1996:'babynames\yob1996.txt', 1997:'babynames\yob1997.txt', 1998:'babynames\yob1998.txt', 
1999:'babynames\yob1999.txt', 2000:'babynames\yob2000.txt', 2001:'babynames\yob2001.txt', 2002:'babynames\yob2002.txt', 2003:'babynames\yob2003.txt',2004:'babynames\yob2004.txt', 2005:'babynames\yob2005.txt', 2006:'babynames\yob2006.txt', 2007:'babynames\yob2007.txt', 2008:'babynames\yob2008.txt', 
2009:'babynames\yob2009.txt', 2010:'babynames\yob2010.txt'} 

import csv
def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        list_lists = list(reader)

    return list_lists


def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    doc = year_file.get(year)
    # print(doc) testing
    baby_list = process_file(doc)
    # print(baby_list) testing
    births = []
    for row in baby_list:
        for list in row:
            births.append([3])
                  
    # print(births)

    return sum (births)
   


def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    total_babies = total_births(year)
    
    doc = year_file.get(year)
    # print(doc) testing
    baby_list = process_file(doc)

    for row in baby_list:
        for list in row:
            if [0] == name and [1] == gender:
                total_name = [3]  

    return total_name/total_babies



def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    year_amounts = []
    for value in year_file:
        year_amounts.append(proportion(name, gender, year_file[value]))

    return max(year_amounts)


def main():
    print(process_file('babynames\yob1880.txt'))
    print(total_births(1880))
    print(proportion('allison', 'F', 1997))
    print(highest_year('allison', 'F'))


if __name__ == '__main__':
    main()
