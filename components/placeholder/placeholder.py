from django_components import component

@component.register("placeholder")
class Placeholder(component.Component):
    template_name = "placeholder/placeholder.html"

    ## Informations que l'on pourra passer au composant et qui seront disponibles dans le template html
    def get_context_data(self, title):
        return {
            "title": title,
        }

    ## On lie avec les fichiers CSS et JS précédemment créé grace à la calsse Media
    class Media:
        css = "placeholder/placeholder.css"
        js = "placeholder/placeholder.js"