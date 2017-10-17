from xml.dom.minidom import parse
dom = parse("0078_BREAST_CANCER_SCREENING_METRIC.xml")
for node in dom.getElementsByTagName('ID'):
	
	