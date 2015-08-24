def demandeGraph(self):
	a = []
	b = []
	c = []
	d = []
	e = []
	f = []
	g = []
	h = []
	i = []
	j = []
	sourceperf = urllib.request.urlopen('https://wwwfrance1.systemmonitor.eu.com/api/?apikey=011aa4c86f650fc18ebc146db091efc5&service=list_performance_history&deviceid=' + self.deviceid + '&interval=15').read().decode('iso-8859-1')
	sourceperf = sourceperf.replace("ISO-8859-1","UTF-8")
	sourcedisk = urllib.request.urlopen('https://wwwfrance1.systemmonitor.eu.com/api/?apikey=011aa4c86f650fc18ebc146db091efc5&service=list_drive_space_history&deviceid=' + self.deviceid + '&interval=DAY').read().decode('iso-8859-1')
	sourcedisk = sourcedisk.replace("ISO-8859-1","UTF-8")
	fichierperf = open("rapports/" + self.nomfichier + 'perf.xml', "a")
	fichierperf.writelines(str(sourceperf))
	fichierperf.close()
	fichierdisk = open("rapports/" + self.nomfichier + 'disk.xml', "a")
	fichierdisk.writelines(str(sourcedisk))
	fichierdisk.close()
	nomfichierhtml = self.nomsociete + '_' + self.nomfichier + '_' + mois + annee + '.html'
	nomfichierpdf = self.nomsociete + '_' + self.nomfichier + '_' + mois + annee + '.pdf'



	tree = etree.parse("rapports/" + self.nomfichier + 'perf.xml')

	for element in tree.xpath("/result/cpu_queue/history/data/start"):
		a.append(element.text)


	for element in tree.xpath("/result/cpu_queue/history/data/queue_average"):
		b.append(element.text)

	k ={}
	for el in a and b

	data = Data([
	    Scatter(
	        x=a,
	        y=b
	    )
	])
	plot_url = py.plot(data, filename="rapports/" + mois + annee + self.nomfichier + 'cpu_queue')
	fichier = open("rapports/" + nomfichierhtml, "a")
	fichier.writelines("<div style=\"page-break-inside:avoid;\"><h1> Graphique de file du processeur en fonction du temps : </h1><a href=\"" + plot_url + "\" target=\"_blank\" title=\"\" style=\"display: block; text-align: center;\"><img src=\"" + plot_url + ".png\" alt=\"\" style=\"max-width: 100%;\"  onerror=\"this.onerror=null;this.src=\'https://plot.ly/404.png\';\" /></a><script data-plotly=\"marcantoine:5\"  src=\"https://plot.ly/embed.js\" async></script></div>")
	fichier.close()

	tree = etree.parse("rapports/" + self.nomfichier + 'perf.xml')
	for element in tree.xpath("/result/cpu_load/history/data/start"):
		c.append(element.text)




	for element in tree.xpath("/result/cpu_load/history/data/cpu/load_average"):
		d.append(element.text)

	for element in tree.xpath("/result/cpu_load/history/data/load_average"):
		d.append(element.text)

	data = Data([
	    Scatter(
	        x=c,
	        y=d
	    )
	])
	plot_url = py.plot(data, filename="rapports/" + mois + annee + self.nomfichier + 'load_average')
	fichier = open("rapports/" + nomfichierhtml, "a")
	fichier.writelines("<div style=\"page-break-inside:avoid;\"><h1> Graphique de charge du processeur en fonction du temps : </h1><a href=\"" + plot_url + "\" target=\"_blank\" title=\"\" style=\"display: block; text-align: center;\"><img src=\"" + plot_url + ".png\" alt=\"\" style=\"max-width: 100%;\"  onerror=\"this.onerror=null;this.src=\'https://plot.ly/404.png\';\" /></a><script data-plotly=\"marcantoine:5\"  src=\"https://plot.ly/embed.js\" async></script></div>")
	fichier.close()

	tree = etree.parse("rapports/" + self.nomfichier + 'perf.xml')
	for element in tree.xpath("/result/memory_usage/history/data/start"):
		e.append(element.text)


	for element in tree.xpath("/result/memory_usage/history/data/available_average"):
		f.append(element.text)

	data = Data([
	    Scatter(
	        x=e,
	        y=f
	    )
	])
	plot_url = py.plot(data, filename="rapports/" + mois + annee + self.nomfichier + 'memory_usage')
	fichier = open("rapports/" + nomfichierhtml, "a")
	fichier.writelines("<div style=\"page-break-inside:avoid;\"><h1> Graphique de memoire vive disponible en fonction du temps : </h1><a href=\"" + plot_url + "\" target=\"_blank\" title=\"\" style=\"display: block; text-align: center;\"><img src=\"" + plot_url + ".png\" alt=\"\" style=\"max-width: 100%;\"  onerror=\"this.onerror=null;this.src=\'https://plot.ly/404.png\';\" /></a><script data-plotly=\"marcantoine:5\"  src=\"https://plot.ly/embed.js\" async></script></div>")
	fichier.close()


	tree = etree.parse("rapports/" + self.nomfichier + 'perf.xml')

	for element in tree.xpath("/result/disk_load/disk/history/data/start"):
		g.append(element.text)


	for element in tree.xpath("/result/disk_load/disk/history/data/disk_time_average"):
		h.append(element.text)

	data = Data([
	    Scatter(
	        x=g,
	        y=h
	    )
	])

	plot_url = py.plot(data, filename="rapports/" + mois + annee + self.nomfichier + 'disk_load')
	fichier = open("rapports/" + nomfichierhtml, "a")
	fichier.writelines("<div style=\"page-break-inside:avoid;\"><h1> Graphique de temps d'acces au disque en fonction du temps : </h1><a href=\"" + plot_url + "\" target=\"_blank\" title=\"\" style=\"display: block; text-align: center;\"><img src=\"" + plot_url + ".png\" alt=\"\" style=\"max-width: 100%;\"  onerror=\"this.onerror=null;this.src=\'https://plot.ly/404.png\';\" /></a><script data-plotly=\"marcantoine:5\"  src=\"https://plot.ly/embed.js\" async></script></div>")
	fichier.close()




	tree = etree.parse("rapports/" + self.nomfichier + 'disk.xml')

	for element in tree.xpath("/result/drive/history/data/day"):
		i.append(element.text)


	for element in tree.xpath("/result/drive/history/data/space_used"):
		j.append(element.text)

	data = Data([
	    Scatter(
	        x=i,
	        y=j
	    )
	])
	plot_url = py.plot(data, filename="rapports/" + mois + annee + self.nomfichier + 'space_used')
	fichier = open("rapports/" + nomfichierhtml, "a")
	fichier.writelines("<div style=\"page-break-inside:avoid;\"><h1> Graphique de l'espace disque utilise (en Mo) en fonction du temps : </h1><a href=\"" + plot_url + "\" target=\"_blank\" title=\"\" style=\"display: block; text-align: center;\"><img src=\"" + plot_url + ".png\" alt=\"\" style=\"max-width: 100%;\"  onerror=\"this.onerror=null;this.src=\'https://plot.ly/404.png\';\" /></a><script data-plotly=\"marcantoine:5\"  src=\"https://plot.ly/embed.js\" async></script></div>" + "<style type=\"text/css\">result{margin: 6em 2em 2em 2em;font-size: 0.9em;background-image:url(\'wall2.jpg\');background-attachment: fixed;background-repeat: no-repeat;background-position: top center;word-wrap: break-word;}check{background-color: #F1F1F2;margin: 2em 0em 0em 0em;padding: 1em;display:block;border: 0.1em solid gray;white-space: pre;}description{	background-color: #7D7D7D;font-size: 1.4em;font-family:Arial, Helvetica, sans-serif;color:white;padding:0.8em;font-weight:bold;box-shadow:0.02em 0.1em 0.3em #888;text-align:center;display:inline;line-height:4em;}</style>")
	fichier.close()
	nomfichierhtml="rapports/" + nomfichierhtml
	nomfichierpdf="rapports/" + nomfichierpdf
	pdfkit.from_file(nomfichierhtml,nomfichierpdf)
	os.remove("rapports/" + self.nomfichier + 'disk.xml')
	os.remove("rapports/" + self.nomfichier + 'perf.xml')

