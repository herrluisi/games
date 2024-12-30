import random


def get_phrase():
    phrases = [
        {
            "phrase": "Was würdest du tun, wenn du für einen Tag unsichtbar wärst?",
            "from": "harmlos",
            "to": "extrem illegal"
        },
        {
            "phrase": "Du könntest eine Person für einen Tag kontrollieren. Was tust du?",
            "from": "hilfreich",
            "to": "ausnutzend"
        },
        {
            "phrase": "Du hast die Macht, ein Gesetz zu ändern oder abzuschaffen. Welches ist es?",
            "from": "unbedeutend",
            "to": "gesellschaftlich revolutionär"
        },
        {
            "phrase": "Du wachst auf und hast Superkräfte. Was ist das Erste, was du damit machst?",
            "from": "Alltagshelfer",
            "to": "Machtdemonstration"
        },
        {
            "phrase": "Was würdest du tun, wenn du wüsstest, dass du morgen im Lotto gewinnst?",
            "from": "ruhig bleiben",
            "to": "alles verkaufen"
        },
        {
            "phrase": "Du kannst dich in ein Tier deiner Wahl verwandeln. Was tust du?",
            "from": "Tiere beobachten",
            "to": "Menschen erschrecken"
        },
        {
            "phrase": "Was würdest du tun, wenn du in der Zeit zurückreisen könntest?",
            "from": "kleine Veränderungen vornehmen",
            "to": "die Geschichte drastisch ändern"
        },
        {
            "phrase": "Du könntest jede Person auf der Welt anrufen. Wen rufst du an?",
            "from": "einen Freund",
            "to": "einen Staatsführer"
        },
        {
            "phrase": "Du wachst plötzlich in einem Paralleluniversum auf. Was ist das Erste, was du tust?",
            "from": "herausfinden, wo du bist",
            "to": "die neue Welt übernehmen"
        },
        {
            "phrase": "Du kannst dir eine Superkraft aussuchen. Welche wählst du?",
            "from": "nützlich",
            "to": "destruktiv"
        },
        {
            "phrase": "Was würdest du tun, wenn du nie wieder schlafen müsstest?",
            "from": "etwas Produktives machen",
            "to": "andere ausnutzen"
        },
        {
            "phrase": "Du findest eine Tasche voller Geld. Was machst du?",
            "from": "zur Polizei bringen",
            "to": "alles ausgeben"
        },
        {
            "phrase": "Was würdest du tun, wenn du einen Tag lang König oder Königin wärst?",
            "from": "harmlose Reformen durchführen",
            "to": "alles zu deinem Vorteil ändern"
        },
        {
            "phrase": "Du kannst eine Sache erfinden, die es noch nicht gibt. Was ist es?",
            "from": "hilfreich",
            "to": "gefährlich"
        },
        {
            "phrase": "Du kannst für einen Tag die Gedanken anderer Menschen lesen. Was tust du?",
            "from": "Freunden helfen",
            "to": "Geheimnisse ausnutzen"
        },
        {
            "phrase": "Was würdest du tun, wenn du für einen Tag mit jedem reden könntest – egal, ob lebendig oder tot?",
            "from": "ein Gespräch mit einem Freund führen",
            "to": "geheime Informationen aus der Geschichte beschaffen"
        },
        {
            "phrase": "Du kannst die Welt für 10 Minuten anhalten. Was machst du?",
            "from": "einen kurzen Moment für dich genießen",
            "to": "etwas Verbotenes tun"
        },
        {
            "phrase": "Du findest eine magische Lampe mit einem Dschinn, der dir drei Wünsche gewährt. Was wünschst du dir?",
            "from": "persönliches Glück",
            "to": "endlose Macht"
        },
        {
            "phrase": "Du kannst die Gedanken einer anderen Person für eine Stunde steuern. Was tust du?",
            "from": "jemandem helfen",
            "to": "eine Katastrophe auslösen"
        },
        {
            "phrase": "Was würdest du tun, wenn du für einen Tag wie ein Kind behandelt werden würdest?",
            "from": "die Ruhe genießen",
            "to": "andere Menschen bewusst provozieren"
        },
        {
            "phrase": "Du könntest einen Ort auf der Welt sofort besuchen. Welcher wäre das?",
            "from": "ein ruhiger Ort",
            "to": "ein gefährliches Krisengebiet"
        },
        {
            "phrase": "Du wachst eines Tages auf und hast Zugriff auf die Bankkonten aller Menschen. Was tust du?",
            "from": "nichts verändern",
            "to": "alles an dich reißen"
        },
        {
            "phrase": "Du könntest ein beliebiges Talent über Nacht perfekt beherrschen. Welches ist es?",
            "from": "etwas Kreatives wie Malen",
            "to": "etwas Mächtiges wie Manipulation"
        },
        {
            "phrase": "Was würdest du tun, wenn du in einer Welt ohne Regeln leben würdest?",
            "from": "so weiterleben wie bisher",
            "to": "alles tun, was verboten ist"
        },
        {
            "phrase": "Du kannst einen Gegenstand besitzen, der unendlich oft kopiert werden kann. Was ist es?",
            "from": "etwas Nützliches wie Essen",
            "to": "etwas Gefährliches wie Waffen"
        },
        {
            "phrase": "Du kannst dich für einen Tag mit einem Tier unterhalten. Welches wählst du und warum?",
            "from": "dein Haustier",
            "to": "einen gefährlichen Raubtierführer"
        },
        {
            "phrase": "Du wirst für einen Tag zum reichsten Menschen der Welt. Was machst du?",
            "from": "Geld für Gutes verwenden",
            "to": "alles für dich behalten"
        },
        {
            "phrase": "Du findest einen mysteriösen Schlüssel, welcher alle Türen öffnen kann. Was machst du?",
            "from": "versuchst herauszufinden, wozu er gehört",
            "to": "öffnest absichtlich gefährliche Türen"
        },
        {
            "phrase": "Was würdest du tun, wenn du für 24 Stunden die Schwerkraft kontrollieren könntest?",
            "from": "kleine Experimente machen",
            "to": "Chaos anrichten"
        },
        {
            "phrase": "Du kannst die Fähigkeit erlangen, alle Sprachen der Welt zu sprechen. Was machst du damit?",
            "from": "Reisen und neue Kulturen kennenlernen",
            "to": "Geheimnisse und Pläne anderer aufdecken"
        },
        {
            "phrase": "Du findest ein Tagebuch, das die Zukunft vorhersagt. Was machst du?",
            "from": "es neugierig lesen",
            "to": "die Informationen für deinen Vorteil nutzen"
        },
        {
            "phrase": "Du kannst für einen Tag deinen Job oder deine Pflichten tauschen. Mit wem tauschst du?",
            "from": "einem Freund oder Kollegen",
            "to": "einer berühmten oder mächtigen Person"
        },
        {
            "phrase": "Du hast die Möglichkeit, eine historische Veranstaltung zu beeinflussen. Was änderst du?",
            "from": "eine kleine positive Änderung machen",
            "to": "die Geschichte radikal umschreiben"
        },
        {
            "phrase": "Du kannst das Wetter für einen Tag weltweit bestimmen. Was machst du?",
            "from": "angenehmes Wetter schaffen",
            "to": "Naturkatastrophen auslösen"
        },
        {
            "phrase": "Du bekommst die Fähigkeit, dich für einen Tag zu teleportieren. Wohin gehst du?",
            "from": "zu einem Traumziel",
            "to": "an einen gefährlichen oder verbotenen Ort"
        },
        {
            "phrase": "Du kannst für einen Tag in einen Film oder ein Buch eintauchen. Welches wählst du?",
            "from": "eine entspannte, lustige Geschichte",
            "to": "eine gefährliche oder düstere Welt"
        },
        {
            "phrase": "Du kannst für einen Tag ein Musiker, Schauspieler oder Künstler sein. Wen wählst du?",
            "from": "einen talentierten Künstler",
            "to": "einen kontroversen Star"
        },
        {
            "phrase": "Du wachst eines Morgens auf und bist berühmt. Was machst du?",
            "from": "versuchst, die Aufmerksamkeit zu genießen",
            "to": "nutzt die Berühmtheit rücksichtslos aus"
        },
        {
            "phrase": "Du kannst eine geheime Organisation gründen. Worum geht es?",
            "from": "etwas Hilfreiches wie Umweltschutz",
            "to": "etwas Gefährliches wie Weltherrschaft"
        },
        {
            "phrase": "Du kannst eine Person aus der Vergangenheit ins heutige Leben bringen. Wen wählst du?",
            "from": "eine inspirierende historische Figur",
            "to": "eine kontroverse oder gefährliche Person"
        },
        {
            "phrase": "Du hast Zugriff auf ein Portal in eine andere Dimension. Was machst du?",
            "from": "vorsichtig erkunden",
            "to": "alles riskieren und eintreten"
        },
        {
            "phrase": "Du kannst für einen Tag in den Körper eines Tieres schlüpfen. Welches Tier wählst du?",
            "from": "ein friedliches Haustier",
            "to": "ein gefährliches Raubtier"
        },
        {
            "phrase": "Du hast die Möglichkeit, einen Prominenten auf einen Kaffee einzuladen. Wen wählst du?",
            "from": "jemanden, den du bewunderst",
            "to": "jemanden, der für Konflikte bekannt ist"
        },
        {
            "phrase": "Du kannst ein beliebiges Geheimnis auf der Welt erfahren. Welches ist es?",
            "from": "ein wissenschaftliches Rätsel",
            "to": "eine politische Verschwörung"
        },
        {
            "phrase": "Du kannst einen Tag lang jeden Job der Welt machen. Welchen wählst du?",
            "from": "etwas Interessantes wie ein Pilot",
            "to": "etwas Mächtiges wie ein Staatsoberhaupt"
        },
        {
            "phrase": "Du hast die Möglichkeit, ein berühmtes Kunstwerk zu verändern. Was machst du?",
            "from": "etwas Kleines hinzufügen",
            "to": "das ganze Werk umgestalten"
        },
        {
            "phrase": "Du kannst die Farbe des Himmels für einen Tag ändern. Welche wählst du?",
            "from": "etwas Beruhigendes wie Pastelltöne",
            "to": "etwas Unheimliches wie Blutrot"
        },
        {
            "phrase": "Du kannst einen Tag in der Zukunft verbringen. Was machst du dort?",
            "from": "Technologie erkunden",
            "to": "Informationen sammeln, um die Gegenwart zu beeinflussen"
        },
        {
            "phrase": "Du kannst für einen Tag der beste Sportler der Welt in einer Sportart sein. Welche wählst du?",
            "from": "eine persönliche Lieblingssportart",
            "to": "eine gefährliche oder extreme Sportart"
        },
        {
            "phrase": "Du kannst für einen Tag ein Objekt lebendig machen. Welches ist es?",
            "from": "etwas Nützliches wie dein Computer",
            "to": "etwas Unheimliches wie eine Puppe"
        },
        {
            "phrase": "Du bekommst die Fähigkeit, für einen Tag durch Wände zu gehen. Was machst du?",
            "from": "neugierig Räume erkunden",
            "to": "Geheimnisse oder verbotene Orte betreten"
        },
        {
            "phrase": "Du kannst einen Gegenstand unendlich oft herstellen lassen. Welcher ist es?",
            "from": "etwas Praktisches wie Essen",
            "to": "etwas Wertvolles wie Gold"
        },
        {
            "phrase": "Du könntest für einen Tag die Rollen in deiner Familie tauschen. Was machst du?",
            "from": "eine entspannte Rolle übernehmen",
            "to": "die Kontrolle übernehmen und Regeln ändern"
        },
        {
            "phrase": "Du kannst für einen Tag der Anführer einer Nation sein. Welche wählst du?",
            "from": "eine friedliche Nation",
            "to": "eine Krisenregion"
        },
        {
            "phrase": "Du hast plötzlich die Fähigkeit, Gedanken laut hörbar zu machen. Was tust du?",
            "from": "Freunden oder Familie zuhören",
            "to": "Geheimnisse oder Pläne anderer enthüllen"
        },
        {
            "phrase": "Du kannst für einen Tag jede Maschine auf der Welt kontrollieren. Was machst du?",
            "from": "hilfreiche Prozesse automatisieren",
            "to": "eine globale Störung verursachen"
        },
        {
            "phrase": "Du bekommst die Macht, ein Naturgesetz zu ändern. Was änderst du?",
            "from": "etwas Kleines wie die Schwerkraft",
            "to": "etwas Großes wie Zeitreisen ermöglichen"
        },
        {
            "phrase": "Du kannst für einen Tag die Träume anderer Menschen sehen. Was machst du?",
            "from": "dich inspirieren lassen",
            "to": "persönliche Geheimnisse herausfinden"
        },
        {
            "phrase": "Du findest ein Buch, in dem dein ganzes Leben steht. Was machst du?",
            "from": "es neugierig lesen",
            "to": "es umschreiben"
        },
        {
            "phrase": "Du kannst für einen Tag alles essen, ohne davon satt zu werden. Was isst du?",
            "from": "leckere Speisen ausprobieren",
            "to": "extreme oder teure Delikatessen"
        },
        {
            "phrase": "Du wachst plötzlich als Zeichentrickfigur in einer Serie auf. Welche Serie wählst du?",
            "from": "eine entspannte Serie",
            "to": "eine gefährliche oder actionreiche Serie"
        },
        {
            "phrase": "Du kannst für einen Tag das Wetter bestimmen. Wie sieht es aus?",
            "from": "angenehm sonnig",
            "to": "chaotisch mit Stürmen"
        },
        {
            "phrase": "Du kannst für einen Tag so schnell laufen wie der Wind. Was machst du?",
            "from": "die Welt erkunden",
            "to": "an gefährlichen oder illegalen Rennen teilnehmen"
        },
        {
            "phrase": "Du wachst eines Tages auf und hast die Stimme eines berühmten Sängers. Was tust du?",
            "from": "Freunde beeindrucken",
            "to": "bei einem Konzert auftreten"
        },
        {
            "phrase": "Du kannst die Form eines Objekts für einen Tag verändern. Welches Objekt wählst du?",
            "from": "etwas Alltägliches wie Möbel",
            "to": "etwas Mächtiges wie ein Gebäude"
        },
        {
            "phrase": "Du kannst für einen Tag ein berühmtes historisches Ereignis miterleben. Welches wählst du?",
            "from": "eine friedliche Entdeckung",
            "to": "eine gefährliche Schlacht"
        },
        {
            "phrase": "Du kannst für einen Tag in einem Märchen leben. Welches wählst du?",
            "from": "ein glückliches und friedliches Märchen",
            "to": "ein düsteres oder gefährliches Märchen"
        },
        {
            "phrase": "Du kannst ein beliebiges Verkehrsmittel erfinden. Wie sieht es aus?",
            "from": "etwas Praktisches wie ein schnelles Auto",
            "to": "etwas Verrücktes wie ein fliegendes Haus"
        },
        {
            "phrase": "Du kannst für einen Tag alles im Fernsehen ändern. Was machst du?",
            "from": "deine Lieblingsserien verlängern",
            "to": "alles komplett umgestalten"
        },
        {
            "phrase": "Du kannst für einen Tag so groß wie ein Hochhaus werden. Was machst du?",
            "from": "die Welt aus einer neuen Perspektive sehen",
            "to": "eine Stadt in Chaos versetzen"
        },
        {
            "phrase": "Du kannst für einen Tag alle Haustiere verstehen. Was machst du?",
            "from": "dein eigenes Haustier besser kennenlernen",
            "to": "Geheimnisse anderer Haustiere erfahren"
        },
        {
            "phrase": "Du kannst für einen Tag wie ein Geist durch Wände gehen. Was machst du?",
            "from": "neugierig neue Orte erkunden",
            "to": "illegale oder gefährliche Orte betreten"
        },
        {
            "phrase": "Du kannst für einen Tag jedes Instrument perfekt spielen. Welches wählst du?",
            "from": "ein klassisches Instrument wie Klavier",
            "to": "etwas Ungewöhnliches wie ein Theremin"
        },
        {
            "phrase": "Du kannst für einen Tag eine berühmte Person sein. Wen wählst du?",
            "from": "eine inspirierende Figur",
            "to": "jemanden Kontroverses"
        },
        {
            "phrase": "Du kannst für einen Tag alle Verkehrsmittel auf der Welt steuern. Was machst du?",
            "from": "die Organisation verbessern",
            "to": "das Chaos maximieren"
        },
        {
            "phrase": "Du kannst für einen Tag die Träume aller Menschen kontrollieren. Was machst du?",
            "from": "positive Träume erschaffen",
            "to": "Albträume verbreiten"
        },
        {
            "phrase": "Du kannst für einen Tag mit einem Prominenten deiner Wahl befreundet sein. Wen wählst du?",
            "from": "eine entspannte Person",
            "to": "eine kontroverse oder schwierige Person"
        },
        {
            "phrase": "Du findest eine Maschine, die jedes Problem lösen kann. Was machst du?",
            "from": "kleine Alltagsprobleme lösen",
            "to": "weltweite Konflikte beeinflussen"
        },
        {
            "phrase": "Du wachst plötzlich als Milliardär auf. Was machst du?",
            "from": "das Geld für gute Zwecke verwenden",
            "to": "alles für dich behalten"
        },
        {
            "phrase": "Du kannst für einen Tag jede Sprache der Welt sprechen. Was machst du?",
            "from": "neue Kulturen kennenlernen",
            "to": "Geheimnisse und Pläne anderer verstehen"
        },
        {
            "phrase": "Du kannst für einen Tag ein Erfinder sein. Was würdest du erfinden?",
            "from": "etwas Hilfreiches",
            "to": "etwas Weltveränderndes"
        },
        {
            "phrase": "Du kannst für einen Tag jeden Beruf ausüben. Welchen wählst du?",
            "from": "einen kreativen Job",
            "to": "etwas Mächtiges wie CEO sein"
        },
        {
            "phrase": "Du kannst für einen Tag die Gesetze der Physik brechen. Was machst du?",
            "from": "Schweben oder Fliegen",
            "to": "Chaos in der Wissenschaft verursachen"
        },
        {
            "phrase": "Du kannst für einen Tag eine Statue zum Leben erwecken. Welche wählst du?",
            "from": "eine friedliche Statue",
            "to": "eine mächtige oder furchteinflößende Statue"
        },
        {
            "phrase": "Du kannst für einen Tag das Internet kontrollieren. Was machst du?",
            "from": "positive Inhalte verbreiten",
            "to": "alles lahmlegen oder manipulieren"
        }
    ]

    return random.choice(phrases)