UNITS_TEXT = """
m2
fft
u
ens
rlx
ml
h
j
kg
"""

LIST_TEXT = """
{"lot": "Préparation sols", "designation": "Dépose revêtement", "unite": "m2", "description": "Dépose de revêtement de sol Type :"}
{"lot": "Préparation sols", "designation": "Ragréage", "unite": "m2", "description": "Dépoussièrement, primaire et mise en oeuvre d'un ragréage Epaisseur (entre 3 et 10 mm) :"}
{"lot": "Préparation sols", "designation": "Ragréage fibré", "unite": "m2", "description": "Dépoussièrement, primaire et mise en oeuvre d'un ragréage FIBRE Epaisseur (entre 3 et 30 mm) :"}
{"lot": "Préparation sols", "designation": "Plus value primaire sur plancher bois", "unite": "m2", "description": "Plus value pour mise en uvre d'un primaire sur support bois type Bostik"}
{"lot": "Préparation sols", "designation": "Panneau OSB", "unite": "m2", "description": "Dépose, fourniture et pose d'un panneau OSB 3, compris bande résiliante sur solive Epaisseur (entre 22 et 28 mm) :"}
{"lot": "Revêtement de sol souple", "designation": "Moquette en dalles", "unite": "m2", "description": "Dépose, Fourniture et Pose d'une moquette en dalles Pose : Dimensions dalles : Qualité : Type de support :"}
{"lot": "Revêtement de sol souple", "designation": "Moquette en lés", "unite": "m2", "description": "Dépose, Fourniture et Pose d'une moquette en lés Pose : collée Qualité : Type de support :"}
{"lot": "Revêtement de sol souple", "designation": "Sol souple jonc de mer/ Sisal", "unite": "m2", "description": "Dépose, Fourniture et pose de jonc de mer / sisal Pose : collée Qualité : Type de support :"}
{"lot": "Revêtement de sol souple", "designation": "Sol PVC dalles", "unite": "m2", "description": "Dépose, Fourniture et Pose de sol PVC en dalles Type pose (collé / clipsé) : Sous couche (sans / intégrée) : Dimensions dalles : Qualité : Type de support :"}
{"lot": "Revêtement de sol souple", "designation": "Sol PVC en lés", "unite": "m2", "description": "Dépose, Fourniture et Pose de sol PVC en lés Pose : collée Qualité : Type de support :"}
{"lot": "Revêtement de sol souple", "designation": "Sol PVC Lame", "unite": "m2", "description": "Dépose, Fourniture et Pose de sol PVC en Lame Type pose (collé / clipsé) : Sous couche (sans / intégrée) : Dimensions lame : Qualité : Type de support :"}
{"lot": "Parquet", "designation": "Parquet stratifié flottant", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un parquet stratifié en pose flottante. compris sous couche. Type de sous couche : Type de pose : Nbre de frise : Chanfrein (0/2/4) : Epaisseur : Largeur : Longueur : Type de support :"}
{"lot": "Parquet", "designation": "Parquet contrecollé flottant", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un parquet contrecollé flottant. compris sous couche. Type sous couche : Type de pose : Essence : Nbre de frise : Chanfrein (0/2/4) : Epaisseur : Largeur : Longueur : Type de support :"}
{"lot": "Parquet", "designation": "Parquet contrecollé collé", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un parquet contrecollé collé Type de pose : Essence : Nbre de frise : Chanfrein (0/2/4) : Epaisseur : Largeur : Longueur : Type de support :"}
{"lot": "Parquet", "designation": "Parquet massif sur lambourde", "unite": "m2", "description": "Dépose, fourniture et pose d'un parquet massif cloué, y compris vitrification si besoin Type de pose : Essence : Epaisseur : Largeur : Longueur : Finition (brut ou finis d'usine) : Chanfrein (0/2/4) : Type de support :"}
{"lot": "Parquet", "designation": "Parquet massif collé", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un parquet massif collé, y compris vitrification si besoin Type de pose : Essence : Epaisseur : Largeur : Longueur : Finition (brut ou finis d'usine) : Chanfrein (0/2/4) : Type de support :"}
{"lot": "Parquet", "designation": "Plus value seuil en lame de parquet", "unite": "ml", "description": "Fourniture et pose d'un seuil en parquet massif de même nature Epaisseur : Largeur : Longueur :"}
{"lot": "Parquet", "designation": "Ponçage/Vitrification", "unite": "m2", "description": "Vitrification du parquet y compris ponçage et préparation Aspect : Type de parquet existant : Info pour assuré : En cas de chanfrein, celui ci sera diminué ou supprimer"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Chaudiere", "unite": "unite", "description": "Remplacement de chaudière, raccordement sur alimentation existante Type : Puissance : Modele :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Radiateur à eau", "unite": "unite", "description": "Remplacement de radiateur à eau, raccordement sur alimentation existante Type : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Radiateur sèche serviette", "unite": "unite", "description": "Remplacement de radiateur à eau sèche serviette, raccordement sur alimentation existante Type : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Réseau chauffage", "unite": "ml", "description": "Remplacement tuyau circuit de chauffage, raccordement sur élement chauffage Type :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Ballon d'eau chaude", "unite": "unite", "description": "Remplacement de ballon d'eau chaude, raccordement sur alimentation existante Type : Positionnement : Volume stockage : Marque :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "WC posé au sol", "unite": "unite", "description": "Remplacement de WC posé au sol, raccordement sur alimentation et évacuation existante Marque : Couleur :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "WC suspendu", "unite": "unite", "description": "Remplacement de WC suspendu avec bati support, plaque, coffrage et cuvette, raccordement sur alimentation et évacuation existante Marque : Couleur :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Lave main", "unite": "unite", "description": "Remplacement de Lave main, raccordement sur alimentation et évacuation existante Marque : Couleur : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Lavabo sur pied", "unite": "unite", "description": "Remplacement de Lavabo sur pied, raccordement sur alimentation et évacuation existante Marque : Couleur : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Vasque suspendu", "unite": "unite", "description": "Remplacement de vasque suspendu, raccordement sur alimentation et évacuation existante Marque : Couleur : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Meuble vasque", "unite": "unite", "description": "Remplacement de meuble sous vasque, compris dépose repose vasque et robinetterie, raccordement sur alimentation et évacuation existante Marque : Couleur : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Robinetterie lavabo", "unite": "unite", "description": "Remplacement robinetterie, raccordement sur alimentation Type : Marque : Couleur :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Bac de douche", "unite": "unite", "description": "Remplacement bac de douche compris joint silicone Type : Marque : Couleur : Dimensions"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Paroi de douche", "unite": "unite", "description": "Remplacement paroi vitré de douche compris joint silicone Type ouvrant : Marque : Couleur ossature : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Robinetterie de douche", "unite": "unite", "description": "Remplacement robinetterie, raccordement sur alimentation Type : Marque : Couleur :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Evier", "unite": "unite", "description": "Remplacement évier compris raccordement évacuation Type : Type de pose : Marque : Teinte : Dimensions :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Réseau eau froide", "unite": "ml", "description": "Remplacement tuyau circuit d'eau froide, raccordement sur élement sanitaire Type :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "Réseau eau chaude", "unite": "ml", "description": "Remplacement tuyau circuit d'eau chaude, raccordement sur élement sanitaire Type :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "VMR", "unite": "unite", "description": "Remplacement bouche VMR, raccordemement sur alimentation existante Type :"}
{"lot": "Plomberie - Sanitaire - Chauffage - VMC", "designation": "VMC", "unite": "unite", "description": "Remplacement VMC, raccordemement sur alimentation existante Emplacement groupe : Nombre de Bouche :"}
{"lot": "Parquet", "designation": "Plus value découpe particulière", "unite": "ens", "description": "Plus value découpe au droit des éléments suivants : -"}
{"lot": "Information", "designation": "Vitrification - Teinte", "unite": "", "description": "Assuré informé qu’une différence de teinte sera perceptible avec les parties conservées non vitrifiées"}
{"lot": "Préparation sols", "designation": "Sous-couche acoustique", "unite": "m2", "description": "Fourniture et pose d'une sous couche acoustique type :"}
{"lot": "Parquet", "designation": "Mise en teinte", "unite": "m2", "description": "Application d'une mise en teinte du parquet avant vitrification afin d’harmoniser la couleur avec un parquet existant"}
{"lot": "Préparation peint", "designation": "Dépose revêtement muraux", "unite": "m2", "description": "Dépose de revêtement muraux Type : Nbre de pans :"}
{"lot": "Peinture", "designation": "Gouttelette / crépi", "unite": "m2", "description": "Préparation et Application de revêtement à la machine Pas de reprise partiel, uniquement par mur/plafond complet Type : Teinte / Aspect : nombre de pan :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Papier peint intissé / standard", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un papier peint intissé / standard Nbre de pans : Avec motif :"}
{"lot": "Carrelage - Faïence", "designation": "Etanchéité (sol)", "unite": "m2", "description": "Application d'un système d'étanchéite Liquide (S.E.L.)"}
{"lot": "Accessoire sol", "designation": "Dépose d'element", "unite": "m2", "description": "Dépose d'élement Type :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Isolation", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un isolant Type isolant : Epaisseur : Extérieur / pièce mitoyenne :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Rabotage, remise en jeu porte", "unite": "unite", "description": "Réalisation d'un rabotage et d'une remise en jeu d'une porte, non compris peinture Matériaux : Dimensions :"}
{"lot": "Menuiserie extérieure – Serrurerie", "designation": "Fenêtre", "unite": "unite", "description": "Dépose, fourniture et pose d'une menuiserie extérieure comprenant : Type de pose : Matériaux : Dimensions hors tout : Nbre de vantaux : Type d'ouvrants : Dimension ouvrant : Finitions : Petits bois : Type de poignée : Vitrage : Entrée d'air :"}
{"lot": "Électricité CF/cf", "designation": "Goulotte électrique", "unite": "ml", "description": "Remplacement de goulotte PVC Section : Teinte :"}
{"lot": "Manutention", "designation": "Luminaire/bouche VMC/Détecteur de fumée/Etc...", "unite": "ens", "description": "Dépose/repose ou protection : - Nbre Luminaire : - Nbre Bouche VMC : - Nbre Détecteur de fumée : - Nbre interphone/sonnette :"}
{"lot": "Autre", "designation": "Plus value protection", "unite": "ens", "description": "Plus value protection de :"}
{"lot": "Asséchement / Travaux préparatoire", "designation": "Grattage des supports", "unite": "m2", "description": "Intervention d'un technicien spécialisé afin de gratter le support pour permettre un séchage naturel y compris déplacement des meubles si besoin, protection et nettoyage."}
{"lot": "Préparation peint", "designation": "Traitement fissure", "unite": "ml", "description": "Ouverture et traitement fissure"}
{"lot": "Peinture", "designation": "Plafonds sinistrés", "unite": "m2", "description": "Application de 2 couches de peinture Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Papier peint vinyle / lessivable", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un papier peint vinyle / lessivable Nbre de pans : Avec motif :"}
{"lot": "Carrelage - Faïence", "designation": "Natte de désolidarisation", "unite": "m2", "description": "Fourniture et pose d'une natte de désolidarisation"}
{"lot": "Accessoire sol", "designation": "Barre de seuil métallique", "unite": "unite", "description": "Dépose, fourniture et pose de barre de seuil Pose : Matière : métallique Couleur : Rattrapage de niveau : Longueur :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Moulure polystyrène", "unite": "ml", "description": "Dépose, fourniture et pose de moulure polystyrene à peindre, Type : Nbre de pans : Dimensions :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Porte Paliere", "unite": "unite", "description": "Remplacement de porte d'entrée de logement, compris réemploi de la quincaillerie. Bati remplacé : Dimensions vantail : Sens ouverture : Finition : Nbre de points : Blindage : Divers (judas, etc"}
{"lot": "", "designation": "", "unite": "", "description": ""}
{"lot": "Menuiserie extérieure – Serrurerie", "designation": "Quincaillerie", "unite": "unite", "description": "Remplacement de quincaillerie Type : Matériau :"}
{"lot": "Électricité CF/cf", "designation": "Radiateur", "unite": "unite", "description": "Remplacement de radiateur électrique, raccordement sur alimentation existante Puissance : Teinte : Dimensions :"}
{"lot": "Manutention", "designation": "Lustre", "unite": "unite", "description": "Dépose/repose ou protection lustre à 2 techniciens"}
{"lot": "Autre", "designation": "Echafaudage hauteur sup 3 m", "unite": "unite", "description": "Mise en place d'un échafaudage pour travaux en hauteur sup à 3 m (par piece)"}
{"lot": "Asséchement / Travaux préparatoire", "designation": "Dépose de TDV / PP", "unite": "m2", "description": "Intervention d'un technicien spécialisé afin de déposer les revêtements muraux de type toile de verre et/ou papier-peint pour permettre un séchage naturel y compris déplacement des meubles si besoin, protection et nettoyage."}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Dalle polystyrène", "unite": "m2", "description": "Dépose, fourniture et pose de dalle polystyrène Finition : Dimensions : (attention au moulure périphérique)"}
{"lot": "Préparation peint", "designation": "Bande calicot", "unite": "ml", "description": "Mise en oeuvre ou reprise de bandes calicot"}
{"lot": "Peinture", "designation": "Plafonds Harmonisations", "unite": "m2", "description": "Mise en peinture pour harmonisation Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Papier peint gamme supérieure", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un papier peint gamme supérieure Nbre de pans : Avec motif :"}
{"lot": "Carrelage - Faïence", "designation": "Carrelage", "unite": "m2", "description": "Dépose, Fourniture et Pose de carrelage Dimensions carreau : Qualité carreau : Teinte joint : Type de support :"}
{"lot": "Accessoire sol", "designation": "Barre de seuil assortie", "unite": "unite", "description": "Dépose, fourniture et pose de barre de seuil Pose : Type : bois Couleur : assortie Rattrapage de niveau : Longueur :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Moulure plâtre", "unite": "ml", "description": "Dépose, fourniture et pose de moulure plâtre à peindre, Type : Nbre de pans : Dimensions :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Porte intérieure", "unite": "unite", "description": "Remplacement de porte intérieure, compris réemploi de la quincaillerie. Bati remplacé : Type : Finition : Dimensions ouvrant :"}
{"lot": "Électricité CF/cf", "designation": "Radiateur sèche serviette", "unite": "unite", "description": "Remplacement de sèche serviette électrique, raccordement sur alimentation existante Puissance : Teinte : Dimensions :"}
{"lot": "Manutention", "designation": "Radiateur électrique", "unite": "unite", "description": "Dépose/repose radiateur électrique"}
{"lot": "Autre", "designation": "Echafaudage hauteur sup 4,50 m", "unite": "unite", "description": "Mise en place d'un échafaudage pour travaux en hauteur sup à 4,5 m (par piece)"}
{"lot": "Asséchement / Travaux préparatoire", "designation": "Dépose de BA13", "unite": "m2", "description": "Intervention d'un technicien spécialisé afin de déposer les plaques de plâtre/isolant pour permettre un séchage naturel y compris déplacement des meubles si besoin, protection et nettoyage."}
{"lot": "Préparation peint", "designation": "Rebouchage platre", "unite": "m2", "description": "Rebouchage ou reprise plâtre ou MAP Dimension :"}
{"lot": "Peinture", "designation": "Rosace", "unite": "unite", "description": "Application de 2 couches de peinture Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Papier peint haut de gamme", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un papier peint haut de gamme Nbre de pans : Avec motif :"}
{"lot": "Carrelage - Faïence", "designation": "Etanchéité (murs)", "unite": "m2", "description": "Application d'un système de protection à l'eau sous carrelage (S.P.E.C.)"}
{"lot": "Accessoire sol", "designation": "Profil d'arrêt carrelage", "unite": "ml", "description": "Fourniture et pose de profils d'arrêt de carrelage Type : Teinte :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Dépose revêtement", "unite": "m2", "description": "Dépose de revêtement Type :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Quincaillerie", "unite": "unite", "description": "Remplacement de quincaillerie Type : Matériau :"}
{"lot": "Électricité CF/cf", "designation": "Prise courant", "unite": "unite", "description": "Remplacement de prise de courant simple, raccordement sur alimentation existante Type : Teinte :"}
{"lot": "Manutention", "designation": "Radiateur à eau", "unite": "unite", "description": "Dépose/repose radiateur à eau non collectif Dimensions :"}
{"lot": "Autre", "designation": "Echafaudage escalier", "unite": "unite", "description": "Mise en place d'un échafaudage escalier Largeur : Hauteur au point le plus haut :"}
{"lot": "Asséchement / Travaux préparatoire", "designation": "Dépose du revêtement sol", "unite": "m2", "description": "Intervention d'un technicien spécialisé afin de déposer les revêtements de sol pour permettre un séchage naturel y compris déplacement des meubles si besoin, protection et nettoyage."}
{"lot": "Préparation peint", "designation": "Enduit standard", "unite": "m2", "description": "Grattage, application enduit 1 à 2 passes, ponçage et impression"}
{"lot": "Peinture", "designation": "Corniche", "unite": "ml", "description": "Application de 2 couches de peinture Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Frise", "unite": "ml", "description": "Retour prod : trop de SAV sur les frises adhésives A validé avec assuré : Prévoir le remplacement papier peint tous pans de murs toute hauteur avec 1 seul référence sans frise"}
{"lot": "Carrelage - Faïence", "designation": "Faience", "unite": "m2", "description": "Dépose, Fourniture et pose de Faience Nbre de pans : Hauteur : Dimensions carreau : Qualité carreau : Teinte joint : Type de support :"}
{"lot": "Accessoire sol", "designation": "Plinthe à peindre", "unite": "ml", "description": "Dépose, fourniture et pose de plinthes bois + peindre Type de bord : Hauteur : Epaisseur : Teinte / Aspect :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Plaque de plâtre collée", "unite": "m2", "description": "Dépose, fourniture et pose de plaques de plâtre collées y compris bandes, joints, enduit et impression Type de plaque : Epaisseur : Nbre élement electrique :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Porte de placard", "unite": "unite", "description": "Remplacement de porte de placard compris rail inférieur et supérieur Nbre de vantaux : Dimensions : Finition :"}
{"lot": "Électricité CF/cf", "designation": "Interrupteur", "unite": "unite", "description": "Remplacement d'interrupteur, raccordement sur alimentation existante Type : Teinte : Gamme :"}
{"lot": "Manutention", "designation": "Manutention mobilier par assuré", "unite": "", "description": "Il a été convenu avec l'assuré qu'il réalisera le déplacement de ses meubles"}
{"lot": "Autre", "designation": "Demande Assuré", "unite": "", "description": "Demande de prise en charge à la demande de l'assuré (Pour CC : à indiquer dans le devis et transmettre l'information à la Diffusion) : -"}
{"lot": "Peinture", "designation": "Murs / Rampants sinistrés", "unite": "m2", "description": "Application de 2 couches de peinture Nbre de pans : Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Papier peint + peinture", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un papier peint à peindre + peinture Nbre de pans : Teinte / Aspect :"}
{"lot": "Carrelage - Faïence", "designation": "Frise de faience", "unite": "ml", "description": "Fourniture et pose de frise en faience Dimensions carreau : Qualité carreau : Teinte joint :"}
{"lot": "Accessoire sol", "designation": "Plinthe revêtue d'un revêtement blanc", "unite": "ml", "description": "Dépose, fourniture et pose de plinthes bois finition blanc Type de bord : Hauteur :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Plaque de plâtre sur ossature conservée", "unite": "m2", "description": "Dépose, fourniture et pose de plaques de plâtre sur ossature conservée y compris bandes, joints, enduit et impression Type de plaque : Epaisseur plaque : Nbre élément électrique :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Aménagement de placard", "unite": "ens", "description": "Remplacement de l'aménagement d'un placard Dimensions : Type :"}
{"lot": "Électricité CF/cf", "designation": "Sortie/alimentation électrique", "unite": "unite", "description": "Remplacement de sortie de cable, raccordement sur alimentation existante Teinte :"}
{"lot": "Manutention", "designation": "Déplacement meubles", "unite": "ens", "description": "Déplacement de meubles, personne PMR ou agée. Lieu stockage (pièce) : Phasage (oui/non) : Sans démontage : Avec démontage :"}
{"lot": "Préparation peint", "designation": "Redressement plâtre ou map", "unite": "m2", "description": "Grattage, application enduit 3 à 4 passes ou au map, ponçage et impression"}
{"lot": "Préparation peint", "designation": "Toile à enduire", "unite": "m2", "description": "Dépose, fourniture et pose d'une toile à enduire compris enduit et impression"}
{"lot": "Peinture", "designation": "Murs / Rampants harmonisations", "unite": "m2", "description": "Mise en peinture pour harmonisation Nbre de pans : Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Toile de verre + peinture", "unite": "m2", "description": "Dépose, Fourniture et Pose d'une toile de verre + peinture Nbre de pans : Teinte Aspect : Motif :"}
{"lot": "Carrelage - Faïence", "designation": "Profil d'angle faïence", "unite": "ml", "description": "Fourniture et pose de profils d'angle Type/Matériaux : Teinte :"}
{"lot": "Accessoire sol", "designation": "Plinthe stratifié", "unite": "ml", "description": "Dépose, fourniture et pose de plinthes bois stratifié Type de bord : arrondie Hauteur (58 / 77 mm) :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Plaque de plâtre sur sur ossature neuve", "unite": "m2", "description": "Dépose, fourniture et pose de plaques de plâtre sur ossature neuve y compris bandes, joints, enduit et impression Type de plaque : Epaisseur plaque : Nbre élément électrique :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Plinthe de cuisine", "unite": "ml", "description": "Remplacement plinthe de cuisine Hauteur : Finition :"}
{"lot": "Électricité CF/cf", "designation": "Prise TV", "unite": "unite", "description": "Remplacement de prise TV, raccordement sur alimentation existante Teinte : Gamme :"}
{"lot": "Manutention", "designation": "Demande Déplacement meubles", "unite": "ens", "description": "Demande de déplacement de meubles à l'assurance : Sans démontage : Avec démontage :"}
{"lot": "Préparation peint", "designation": "Impression/Fongicide/ fixateur", "unite": "m2", "description": "Application de la préparation Type :"}
{"lot": "Peinture", "designation": "Demande harmonisation", "unite": "m2", "description": "A la demande de l'assuré : Mise en peinture pour harmonisation Nbre de pans : Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Lambris sur ossature conservée", "unite": "m2", "description": "Dépose, Fourniture et Pose de lambris sur ossature conservée Type : Nbre de pans : Dimensions :"}
{"lot": "Carrelage - Faïence", "designation": "Reprise Joints carrelage/faïence", "unite": "m2", "description": "Curage et mise en oeuvre de joints ciment de carrelage/faïence Teinte :"}
{"lot": "Accessoire sol", "designation": "Plinthe massif", "unite": "ml", "description": "Dépose, fourniture et pose de plinthes bois massif à vitrifier Essence : Type de bord : Hauteur : Epaisseur :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Cloison alvéolaire", "unite": "m2", "description": "Fourniture et pose de cloison alvéolaire compris renfort bois, bandes et joints (hauteur max : 2,70 m) Epaisseur (5 ou 6 cm) : Type de plaque : Nbre élement electrique :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Meuble bas", "unite": "unite", "description": "Remplacement meuble bas, Conservation façade : Hauteur caisson : Largeur Caisson : Profondeur Caisson : Epaisseur panneau : Aménagement (tablette ou tiroir) :"}
{"lot": "Électricité CF/cf", "designation": "Prise RJ45", "unite": "unite", "description": "Remplacement de prise RJ45, raccordement sur alimentation existante Teinte : Gamme :"}
{"lot": "Manutention", "designation": "Déménagement, réaménagement meubles", "unite": "ens", "description": "Déménagement, réaménagement de meubles y compris garde meuble :"}
{"lot": "Peinture", "designation": "Murs décoratif bois avec moulure (soubassement)", "unite": "m2", "description": "Application de 2 couches de peinture Nbre de pans : Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Lambris sur ossature neuve", "unite": "m2", "description": "Dépose, Fourniture et Pose de lambris sur ossature neuve Type : Nbre de pans : Dimensions :"}
{"lot": "Accessoire sol", "designation": "Plinthe décorative (moulurée)", "unite": "ml", "description": "Dépose, fourniture et pose de plinthes bois moulurées Hauteur : Epaisseur : teinte :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Cloison sur ossature", "unite": "m2", "description": "Fourniture et pose de cloison sur ossature métallique y compris bandes et joints Type de plaque : Epaisseur : Nbre élement electrique :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Meuble haut", "unite": "unite", "description": "Remplacement meuble haut, Conservation façade : Hauteur caisson : Largeur Caisson : Profondeur Caisson : Epaisseur panneau : Aménagement (tablette ou tiroir) :"}
{"lot": "Électricité CF/cf", "designation": "Douille DCL", "unite": "unite", "description": "Remplacement de douille DCL, raccordement sur alimentation existante."}
{"lot": "Manutention", "designation": "Elément menuiserie", "unite": "unite", "description": "Dépose/repose élément de menuiserie : Type : Dimensions :"}
{"lot": "Préparation peint", "designation": "Impression isolante pour incendie", "unite": "m2", "description": "Application d'une impression isolante glycéro après décontamination"}
{"lot": "Peinture", "designation": "Plinthes", "unite": "ml", "description": "Application de 2 couches de peinture Nbre de pans : Teinte / Aspect :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Tissus tendu - support conservé", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un tissu tendu agrafé sur lattes bois conservées, y compris molleton Nbre de pans : Teinte :"}
{"lot": "Accessoire sol", "designation": "Plinthes carrelage", "unite": "ml", "description": "Dépose, fourniture et pose de plinthes de carrelage de réf à déterminer Dimensions : Finitions :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Cloison carreau de plâtre", "unite": "m2", "description": "Fourniture et pose de cloison en carreau de plâtre y compris bandes et joints Epaisseur (5, 7 ou 10 cm) : Type de carreaux : Nbre élement electrique :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Meuble colonne", "unite": "unite", "description": "Remplacement meuble colonne, Conservation façade : Hauteur caisson : Largeur Caisson : Profondeur Caisson : Epaisseur panneau : Aménagement (tablette ou tiroir) :"}
{"lot": "Électricité CF/cf", "designation": "Spot encastré", "unite": "unite", "description": "Remplacement de spot encastré, raccordement sur alimentation existante IP : Teinte : Led/halogène :"}
{"lot": "Manutention", "designation": "Elément électrique", "unite": "unite", "description": "Dépose/repose élément électrique : Type : Dimensions :"}
{"lot": "Préparation peint", "designation": "Lessivage", "unite": "m2", "description": "Lessivage de surface avant peinture. Cause :"}
{"lot": "Papier peint - Tissus tendu - Lambris", "designation": "Tissus tendu - support neuf", "unite": "m2", "description": "Dépose, Fourniture et Pose d'un tissu tendu agrafé sur lattes bois, y compris molleton Nbre de pans : Teinte :"}
{"lot": "Accessoire sol", "designation": "Quart de rond à peindre", "unite": "ml", "description": "Dépose, fourniture et pose de quart de rond à peindre Essence : Hauteur :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Faux plafond dalles sur ossature conservée", "unite": "m2", "description": "Dépose, fourniture et pose de dalles minérales de faux plafond de sur ossature métallique conservée Type d'ossature : Dimension dalle : Teinte : Spécificité :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Façade de meuble", "unite": "unite", "description": "Remplacement de facade Dimensions : Finition :"}
{"lot": "Électricité CF/cf", "designation": "Réglette lumineuse", "unite": "unite", "description": "Remplacement de réglette lumineuse, raccordement sur alimentation existante Teinte :"}
{"lot": "Manutention", "designation": "Elément sanitaire", "unite": "unite", "description": "Dépose/repose élément sanitaire : Type : Dimensions :"}
{"lot": "Peinture", "designation": "Quart de rond", "unite": "ml", "description": "Application de 2 couches de peinture Nbre de pans : Teinte / Aspect :"}
{"lot": "Peinture", "designation": "Portes avec bâti", "unite": "unite", "description": "Application de 2 couches de peinture compris bati Nbre de face : Dimensions : Teinte / Aspect :"}
{"lot": "Accessoire sol", "designation": "Quart de rond assortie", "unite": "ml", "description": "Dépose, fourniture et pose de quart de rond assortie Finition : stratifié Hauteur : 14 mm"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Faux plafond dalles sur ossature neuve", "unite": "m2", "description": "Dépose, fourniture et pose de dalles minérales de faux plafond de sur ossature métallique neuve Type d'ossature : Dimsension dalle : Teinte : Spécificité :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Plan de travail", "unite": "unite", "description": "Remplacement de plan de travail Type : Nombre de réservation : Dimensions :"}
{"lot": "Électricité CF/cf", "designation": "Tableau électrique", "unite": "ens", "description": "Remplacement de tableau, raccordement sur alimentation existante Compris repérage de câble Nbre de rangée : Différentiel (Nbre/puissance) : Nbre de dijoncteur 10A : Nbre de dijoncteur 16A : Nbre de dijoncteur 20A : Nbre de dijoncteur 32A :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Crédence", "unite": "ml", "description": "Remplacement de crédence Type : Nombre de réservation : Dimensions :"}
{"lot": "Peinture", "designation": "Bâti de porte", "unite": "unite", "description": "Application de 2 couches de peinture sur bati Nbre de face : Dimensions : Teinte / Aspect :"}
{"lot": "Électricité CF/cf", "designation": "Remplacement tableau électrique sur GTL", "unite": "ens", "description": "Remplacement d'un tableau sur gaine GTL, raccordement sur alimentation existante Compris repérage de câble Nbre de rangée : Différentiel (Nbre/puissance) : Nbre de dijoncteur 10A : Nbre de dijoncteur 16A : Nbre de dijoncteur 20A : Nbre de dijoncteur 32A :"}
{"lot": "Isolation - Cloisonnement - Faux-plafond", "designation": "Coffrage", "unite": "ml", "description": "Remplacement Coffrage compris ossature et isolant 45 mm. Nombre de face : Dimensions : Ep et Type de plaque :"}
{"lot": "Menuiserie intérieure - Agencement", "designation": "Coffrage", "unite": "ml", "description": "Remplacement Coffrage compris ossature et isolant 45 mm. Nombre de face : Dimensions : Ep et Type de plaque :"}
{"lot": "Peinture", "designation": "Fenêtres", "unite": "unite", "description": "Application de 2 couches de peinture Nbre de face : Matériaux : Dimensions : Teinte / Aspect :"}
{"lot": "Électricité CF/cf", "designation": "Saignée", "unite": "ml", "description": "Réalisation d'une saignée pour passage câble compris rebouchage"}
{"lot": "Électricité CF/cf", "designation": "Réseau electricité", "unite": "ml", "description": "Remplacement alimentation électrique Ampérage : Elements :"}
{"lot": "Peinture", "designation": "Bâti de fenêtre", "unite": "unite", "description": "Application de 2 couches de peinture sur fenêtre Nbre de face : Dimensions : Teinte / Aspect :"}
{"lot": "Peinture", "designation": "Radiateurs", "unite": "unite", "description": "Application de 2 couches de peinture Dimensions : Teinte / Aspect :"}
{"lot": "Peinture", "designation": "Tuyaux", "unite": "ml", "description": "Préparation et application de 2 couches de peinture Teinte / Aspect :"}
{"lot": "Peinture", "designation": "Poutre/ Poteau", "unite": "ml", "description": "Application de 2 couches de peinture Nombre de face Teinte / Aspect :"}
"""

RULES_TEXT = """

RÈGLES MÉTIER – CHIFFRAGE ET DESCRIPTION DES PRESTATIONS

================================================================
1. RÈGLES GÉNÉRALES
================================================================

- Toutes les réparations doivent être incluses dans le chiffrage.
- Les réparations sont toujours à la charge de l’assuré, sauf mention contraire explicite.
- Toute prestation vague ou imprécise est interdite.
- Chaque prestation doit permettre une adaptation précise du prix.

================================================================
2. PRÉPARATION PEINTURE
================================================================

- Les prestations de préparation peinture sont distinctes de la mise en peinture.
- Les 25 % de préparation légère sont considérés comme inclus par défaut, sauf mention contraire.
- Toute prestation indiquée comme "en plus des 25 %" doit être chiffrée séparément.

Préparation peinture – règles spécifiques :

- Traitement fissure → rebouchage :
  - 1 mètre linéaire = 0,5 m².
  - Toujours à chiffrer en plus des 25 % de préparation.

- Bande calicot :
  - Toujours à chiffrer en plus des 25 % de préparation.

- Rebouchage plâtre (trou) :
  - Forfait de 1 m² par zone concernée.

- Enduit standard – 2 passes :
  - Si la surface concernée est inférieure à 25 % des surfaces de peinture, la reprise est interdite.
  - Si supérieure ou égale à 25 %, la prestation est autorisée.

- Enduit lourd – 4 passes :
  - Toujours à chiffrer en plus des 25 % de préparation.

- Impression / fongicide :
  - Si la surface concernée est inférieure à 25 % des surfaces de peinture, la reprise est interdite.
  - Si supérieure ou égale à 25 %, la prestation est autorisée.

================================================================
3. PEINTURE
================================================================

- Le type de peinture doit obligatoirement être précisé.
- La formulation générique "préparation + peinture" est interdite.

Prestations peinture autorisées :

- Gouttelette / crépi :
  - Chiffrée en forfait unique par chantier.

- Plafonds sinistrés standard :
  - Peinture satinée, velours ou mate (à préciser).

- Plafonds sinistrés brillante / laquée :
  - Peinture brillante ou laquée (obligatoire de préciser).

- Rosace.
- Corniche.
- Murs / rampants sinistrés.
- Murs / rampants – harmonisation.
- Plinthes.
- Quart de rond.
- Portes avec bâti.
- Bâti de porte seul.
- Fenêtres.
- Bâti de fenêtre.
- Radiateurs.
- Tuyaux.

================================================================
4. PARQUET STRATIFIÉ
================================================================

- Le remplacement doit être total sur l’ensemble de la pièce.
- Le remplacement partiel est interdit.

Règles de surface :

- Surface réelle arrondie au multiple de 5 m² (conditionnement).
- Ou surface réelle seule, selon contexte.
- Ou surface réelle + 10 %, arrondie à l’unité supérieure.

Éléments complémentaires :

- Barre de seuil métallique ou stratifiée à préciser.
- Remplacement des plinthes ou quarts-de-rond obligatoire.

================================================================
5. MOQUETTE
================================================================

- Moquette standard :
  - Surface réelle.

- Conditionnement possible :
  - Largeur de 4 m × longueur de la pièce.

- Si plinthes en bois :
  - Prévoir une prestation de peinture des plinthes.

================================================================
6. SOL SOUPLE
================================================================

- Sol souple standard :
  - Surface réelle.

- Conditionnement possible :
  - Largeur de 2 m, 3 m, 4 m ou 5 m × longueur de la pièce.

- Si plinthes en bois :
  - Prévoir une prestation de peinture des plinthes.

================================================================
7. ACCESSOIRES DE SOL
================================================================

Prestations autorisées :

- Dépose / pose de plinthes.
- Fourniture de plinthes à peindre :
  - Ajouter obligatoirement la prestation peinture.
- Fourniture de plinthes stratifiées.
- Fourniture de plinthes PVC.
- Dépose / pose de quart de rond.
- Fourniture de quart de rond à peindre :
  - Ajouter la peinture sauf si la plinthe est déjà prévue à peindre.
- Fourniture de quart de rond stratifié.

================================================================
8. PAPIER PEINT
================================================================

- Papier peint standard :
  - Comprend 25 % de préparation légère.

Règles de quantités :

- Conditionnement :
  - Rouleaux de 5 m².
  - +1 rouleau obligatoire si papier avec motif.

- Taux de reprise :
  - Minimum 15 % selon zone de dégâts.
  - Maximum 75 %.

================================================================
9. TOILE DE VERRE
================================================================

- Toile mur :
  - Comprend 25 % de préparation légère.
  - Taux de reprise compris entre 25 % minimum et 75 % maximum selon dégâts.

- Toile plafond :
  - Comprend 25 % de préparation légère.
  - Taux de reprise compris entre 25 % minimum et 75 % maximum selon dégâts.

================================================================
10. COHÉRENCE DES PRESTATIONS
================================================================

- Une reprise de support sans finition associée est interdite.
- Toute reprise d’enduit doit être accompagnée :
  - soit d’une mise en peinture,
  - soit d’une finition clairement définie.

"""