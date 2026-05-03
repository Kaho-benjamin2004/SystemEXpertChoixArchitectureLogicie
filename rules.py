def choisir_architecture(data):
    score = {
        "Monolithique": 0,
        "Microservices": 0,
        "MVC": 0,
        "Client-Serveur": 0,
        "Event-Driven": 0,
        "Serverless": 0
    }

    explications = {
        "Monolithique": [],
        "Microservices": [],
        "MVC": [],
        "Client-Serveur": [],
        "Event-Driven": [],
        "Serverless": []
    }

    # Règles + explications

    if data["taille"] == "petit":
        score["Monolithique"] += 2
        explications["Monolithique"].append("""
        📌 Pourquoi ce choix ?
Vous avez interet a choisir une architecture monolithique parce qu’elle permet de développer une application de manière simple et rapide, en regroupant toutes les fonctionnalités dans un seul bloc. Ce choix est particulièrement adapté quand le projet est encore petit ou en phase de démarrage, avec une équipe réduite et des besoins bien définis. Il facilite le développement, les tests, le déploiement et la maintenance initiale, car tout est centralisé dans une seule application, sans la complexité de communication entre plusieurs services. C’est donc une solution efficace pour gagner du temps et réduire la complexité technique au début d’un projet.
""")

    if data["taille"] == "grand":
        score["Microservices"] += 3
        explications["Microservices"].append("""
        📌 Pourquoi ce choix ?
Vous avez interet une architecture microservices lorsque l’application devient grande, complexe ou destinée à évoluer rapidement. Ce choix est motivé par le besoin de diviser le système en plusieurs petits services indépendants, chacun responsable d’une fonctionnalité précise. Cela permet à chaque équipe de travailler séparément sur des parties différentes de l’application, de les développer, tester et déployer sans impacter le reste du système. On privilégie aussi cette architecture quand on a besoin de scalabilité, car chaque service peut être amélioré ou mis à l’échelle indépendamment selon la charge. Elle est donc idéale pour les projets complexes et évolutifs, même si elle introduit plus de complexité dans la gestion et la communication entre services.
""")

    if data["scalabilite"] == "elevee":
        score["Microservices"] += 2
        explications["Microservices"].append("""
        📌 Pourquoi ce choix ?
On choisit une architecture microservices lorsque l’application devient grande, complexe ou destinée à évoluer rapidement. Ce choix est motivé par le besoin de diviser le système en plusieurs petits services indépendants, chacun responsable d’une fonctionnalité précise. Cela permet à chaque équipe de travailler séparément sur des parties différentes de l’application, de les développer, tester et déployer sans impacter le reste du système. On privilégie aussi cette architecture quand on a besoin de scalabilité, car chaque service peut être amélioré ou mis à l’échelle indépendamment selon la charge. Elle est donc idéale pour les projets complexes et évolutifs, même si elle introduit plus de complexité dans la gestion et la communication entre services.
""")

    if data["temps_reel"] == "oui":
        score["Event-Driven"] += 3
        explications["Event-Driven"].append("""
        📌 Pourquoi ce choix ?
On choisit une architecture event-driven (orientée événements) lorsqu’on veut construire des systèmes capables de réagir rapidement à des actions ou changements, sans dépendre directement des autres composants. Ce choix est particulièrement adapté aux applications distribuées, en temps réel ou très scalables, car les services communiquent via des événements (messages) au lieu d’appels directs. Cela permet de découpler fortement les composants : chaque service publie ou consomme des événements de manière indépendante, ce qui améliore la flexibilité, la résilience et la capacité d’évolution du système. On la privilégie aussi lorsque l’on veut gérer de gros volumes de données ou des processus asynchrones, comme dans les systèmes de notification, de trading, d’e-commerce ou d’IoT.""")

    if data["complexite"] == "moyenne":
        score["MVC"] += 2
        explications["MVC"].append("""
        📌 Pourquoi ce choix ?
On choisit l’architecture MVC (Model-View-Controller) pour organiser une application de manière claire et structurée en séparant les responsabilités. Ce choix est idéal lorsqu’on développe des applications web ou des interfaces utilisateur, car il permet de distinguer la logique métier (Model), l’affichage (View) et le contrôle des actions utilisateur (Controller). Cela rend le code plus facile à comprendre, à maintenir et à faire évoluer, surtout quand plusieurs développeurs travaillent sur le même projet. On privilégie MVC quand on veut une bonne organisation du code dès le départ, éviter le mélange entre interface et logique, et faciliter les tests ainsi que les modifications futures.
""")

    if data["utilisateurs"] == "eleve":
        score["Client-Serveur"] += 2
        explications["Client-Serveur"].append("""
        📌 Pourquoi ce choix ?
On choisit l’architecture client-serveur lorsqu’on veut organiser une application où les rôles sont clairement séparés entre un client (qui demande un service) et un serveur (qui fournit le service et les données). Ce choix est très courant car il permet de centraliser les données et la logique métier côté serveur, ce qui facilite la gestion, la sécurité et les mises à jour. Le client, quant à lui, se concentre sur l’interface utilisateur et l’interaction. On l’utilise surtout dans les applications web, mobiles ou réseaux, car il permet à plusieurs utilisateurs d’accéder aux mêmes services de manière efficace et contrôlée.
""")

    if data["budget"] == "faible":
        score["Serverless"] += 2
        explications["Serverless"].append("""
        📌 Pourquoi ce choix ?
On choisit une architecture serverless lorsqu’on veut développer une application sans gérer directement les serveurs. Dans ce modèle, le développeur se concentre uniquement sur le code des fonctionnalités, tandis qu’un fournisseur cloud (comme AWS, Azure ou Google Cloud) s’occupe automatiquement de l’infrastructure, de la mise à l’échelle et de la maintenance. Ce choix est idéal pour les applications avec des charges variables ou imprévisibles, car on ne paie que pour l’exécution réelle du code. On privilégie aussi serverless pour accélérer le développement, réduire les coûts d’infrastructure et éviter la complexité de la gestion des serveurs, surtout pour les API, les microservices légers ou les applications événementielles.

        """)

    # Trouver la meilleure architecture
    meilleure = max(score, key=score.get)

    return meilleure, score, explications[meilleure]