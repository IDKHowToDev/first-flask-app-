from website import create_app
app = create_app()
if __name__ == '__main__':  # uniquement executer l'applicaton si le nom de fichier executer est main
    # le debug est true afin de modifier le site web directement
    app.run(debug=True)
