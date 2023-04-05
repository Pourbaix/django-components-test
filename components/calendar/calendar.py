from django_components import component

@component.register("calendar")
class Calendar(component.Component):
    template_name = "calendar/calendar.html"

    ## Informations que l'on pourra passer au composant et qui seront disponibles dans le template html
    def get_context_data(self, date, message, text):
        return {
            "date": date,
            "message": message,
            "text": text,
        }

    ## On lie avec les fichiers CSS et JS précédemment créé grace à la calsse Media
    class Media:
        css = "calendar/calendar.css"
        js = "calendar/calendar.js"