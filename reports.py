from jinja2 import Environment, FileSystemLoader

def create_report(output_folder, cables, clusters):
    env = Environment(loader=FileSystemLoader("templates"))

    template = env.get_template("index.html")

    cluster_data = []

    for cluster in clusters:
        centroid, distance = sorted(clusters[cluster], key=lambda x: x[1])[0]
        cluster_data.append([cluster, len(clusters[cluster]), cables[centroid].subject()])

    template_data = template.render(cluster_data=cluster_data)

    with open("%s/index.html" % output_folder, "w") as f:
        f.write(template_data)
    
    template = env.get_template("cluster.html")

    for cluster in clusters:
        cluster_data = []
    
        centroid, distance = sorted(clusters[cluster], key=lambda x: x[1])[0]
        subject = cables[centroid].subject()
    
        for item, distance in sorted(clusters[cluster], key=lambda x: x[1]):
            cable = cables[item]
            link_to = "https://wikileaks.org/cable/%d/%02d/%s.html" % (cable.date.year, cable.date.month, cable.refid)
            cluster_data.append([cables[item].subject(), 
                                 link_to, 
                                 cables[item].classification,
                                 cables[item].date])

        template_data = template.render(cluster=cluster, subject=subject, cluster_data=cluster_data)

        with open("%s/cluster_%d.html" % (output_folder, cluster), "w") as f:
            f.write(template_data)
