import xml.etree.ElementTree as ET

tree = ET.parse('forecast.xml')
root = tree.getroot()

class TempratureConverter:
    def convert_celsius_to_fahrenheit(self, celsius):
        fahrenheit = 9/5 * celsius + 32
        return fahrenheit

convert = TempratureConverter()

# print(root.tag)
for item in root:
    # print(item[0].text)
    # print(item[1].text)
    celsius = int(item[1].text)
    print(item[0].text + ': '+ str(celsius) + ' Celsius, ' + str(convert.convert_celsius_to_fahrenheit(celsius)) + " Fahrenheit")