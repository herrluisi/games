import random

def get_gericht():
    gericht = [
    "§611 BGB Arbeitsvertrag",
    "§612 BGB Arbeitsvertrag - Vergütung",
    "§623 BGB Kündigung des Arbeitsvertrags",
    "§626 BGB Außerordentliche Kündigung",
    "§627 BGB Kündigung des Dienstverhältnisses",
    "§629 BGB Auskunftspflicht des Arbeitgebers",
    "§630 BGB Pflichten des Arbeitnehmers",
    "§631 BGB Arbeitsunfähigkeit",
    "§632 BGB Vergütung bei Arbeitsunfähigkeit",
    "§633 BGB Haftung des Arbeitgebers",
    "§634 BGB Mängelhaftung des Arbeitgebers",
    "§635 BGB Schadensersatzpflicht des Arbeitnehmers",
    "§638 BGB Abnahme des Werks",
    "§639 BGB Zahlung der Vergütung für Werkleistungen",
    "§646 BGB Abtretung von Forderungen",
    "§649 BGB Kündigung eines Werkvertrages",
    "§654 BGB Haftung für Mängel des Werkes",
    "§660 BGB Sonderrechte des Arbeitnehmers",
    "§668 BGB Lohnzahlungspflicht des Arbeitgebers",
    "§670 BGB Arbeitsschutz und Betriebsverfassungsrecht",
    "§672 BGB Regelt Bestimmungen zur Lohnfortzahlung",
    "§673 BGB Auflösung des Arbeitsverhältnisses durch Arbeitgeber",
    "§678 BGB Lohn- und Gehaltsforderungen",
    "§692 BGB Schadensersatzpflicht des Arbeitnehmers",
    "§703 HGB Kaufmann im Handelsrecht",
    "§704 HGB Unzulässige Handelspraktiken",
    "§705 HGB Kaufmannsrechtliche Haftung",
    "§709 HGB Verantwortlichkeit für Waren",
    "§710 HGB Betrügerische Markennutzung",
    "§715 HGB Betrieb der Warenkontrolle",
    "§725 HGB Verpflichtungen der Betriebsführung",
    "§752 HGB Verletzung des Geschäftsgeheimnisses",
    "§754 HGB Handelsrechtliche Steuervergehen",
    "§756 HGB Haftung der juristischen Person",
    "§763 HGB Veruntreuung von Kapital",
    "§764 HGB Missbrauch von Firmennamen",
    "§766 HGB Verstöße gegen Handelsgesetze",
    "§770 HGB Missbrauch von Verkaufsrechten",
    "§800 HGB Steuerrechtliche Verstöße",
    "§850 HGB Steuerbetrug durch illegale Gesellschaften",
    "§900 StVG Fahrerflucht nach Unfall",
    "§901 StVG Verstöße gegen Verkehrsregeln",
    "§902 StVG Umfassende Verkehrskontrolle",
    "§903 StVG Unerlaubte Straßenbenutzung",
    "§904 StVG Verstöße gegen Verkehrsordnungen",
    "§905 StVG Missachtung der Beleuchtungspflichten",
    "§906 StVG Gefährdung durch falsches Überholen",
    "§907 StVG Verstöße gegen Fahrzeugzulassung",
    "§908 StVG Gefährliche Handlungen im Straßenverkehr",
    "§909 StVG Drogenmissbrauch im Verkehr",
    "§910 StVG Verstöße gegen Geschwindigkeitsbegrenzungen",
    "§911 StVG Verstöße gegen Ausweispflicht",
    "§912 StVG Ordnungswidrigkeiten im Verkehr",
    "§913 StVG Alkohol im Verkehr",
    "§914 StVG Drogenfahrt im Verkehr",
    "§915 StVG Ordnungswidrigkeiten bei ungesicherten Fahrzeugen",
    "§916 StVG Unerlaubte Nutzung von Fahrzeugen",
    "§951 StVO Straßenverkehrsordnung - Fahren ohne Führerschein",
    "§952 StVO Unzulässige Benutzung von Fahrradwegen",
    "§953 StVO Missachtung der Verkehrszeichen",
    "§954 StVO Verstöße gegen Parkverbot",
    "§955 StVO Unerlaubte Benutzung von Tunnels",
    "§956 StVO Verkehrssicherheitspflicht",
    "§957 StVO Verstöße gegen Straßenbenutzungspflicht",
    "§958 StVO Missachtung der Parkvorschriften",
    "§961 StVO Fahren ohne Zulassung",
    "§962 StVO Verstöße gegen Umweltschutzvorgaben",
    "§963 StVO Verkehrsregelung bei Baustellen",
    "§964 StVO Verstöße bei Motorradverkehr",
    "§965 StVO Missachtung von Abbiegevorschriften",
    "§966 StVO Verstöße gegen Mautvorschriften",
    "§967 StVO Unbefugtes Fahren auf Gehwegen",
    "§1001 WAFFG Waffenbesitz und -handel",
    "§1002 WAFFG Besitz von illegalen Schusswaffen",
    "§1003 WAFFG Verwendung von verbotenen Waffen",
    "§1005 WAFFG Herstellung von illegalen Waffen",
    "§1006 WAFFG Fälschung von Waffenbesitzkarten",
    "§1007 WAFFG Verstöße gegen das Waffenlagerrecht",
    "§1009 WAFFG Illegaler Waffenhandel",
    "§1010 WAFFG Verstöße gegen das Kriegswaffenkontrollgesetz",
    "§1011 WAFFG Unerlaubte Waffenlagerung",
    "§1012 WAFFG Missbrauch von Schusswaffen im Verkehr",
    "§1015 WAFFG Verstöße gegen das Waffenrecht",
    "§1016 WAFFG Besitz und Nutzung von Schusswaffen ohne Erlaubnis",
    "§108 OWIG Ordnungswidrigkeiten im Straßenverkehr",
    "§109 OWIG Ordnungswidrigkeiten im Bereich des Umweltschutzes",
    "§110 OWIG Verstöße gegen die Umweltvorschriften",
    "§111 OWIG Verstöße gegen Sicherheitsvorschriften",
    "§112 OWIG Verstöße gegen Lärmschutzverordnung",
    "§113 OWIG Nichtbeachtung von Rauchverboten",
    "§114 OWIG Verstöße gegen das Abfallrecht",
    "§115 OWIG Verstöße gegen das Naturschutzrecht",
    "§116 OWIG Verstöße gegen das Abfallentsorgungsgesetz",
    "§117 OWIG Verstöße gegen die Pflicht zur Mülltrennung",
    "§118 OWIG Verstöße gegen das Immissionsschutzrecht",
    "§119 OWIG Verstöße gegen das Straßenrecht",
    "§120 OWIG Verstöße gegen das Tierschutzgesetz",
    "§125 BTMG Besitz von Betäubungsmitteln",
    "§126 BTMG Handel mit Betäubungsmitteln",
    "§127 BTMG Herstellung von Betäubungsmitteln",
    "§128 BTMG Schmuggel von Betäubungsmitteln",
    "§129 BTMG Drogenmissbrauch im Verkehr",
    "§130 BTMG Verstöße gegen das Betäubungsmittelrecht",
    "§131 BTMG Verstöße gegen die Vorschriften über den Umgang mit Betäubungsmitteln",
    "§132 BTMG Verstöße gegen das Arzneimittelgesetz",
    "§134 BTMG Handel mit gefährlichen Drogen",
    "§135 BTMG Besitz von Drogen ohne Rezept",
    "§137 BTMG Unerlaubte Drogenaufnahme",
    "§140 BTMG Missbrauch von Drogen für kriminelle Handlungen",
    "§141 BTMG Herstellung und Versand von Drogen",
    "§143 BTMG Drogenfälschung",
    "§144 BTMG Verstöße gegen das Dopinggesetz",
    "§145 BTMG Herstellung von Dopingmitteln",
    "§147 URHG Urheberrechtsverletzung",
    "§149 URHG Verbreitung urheberrechtlich geschützter Werke ohne Genehmigung",
    "§150 URHG Vervielfältigung von urheberrechtlich geschützten Werken",
    "§151 URHG Fälschung von urheberrechtlich geschützten Werken",
    "§152 URHG Nutzung von Musikwerken ohne Genehmigung",
    "§153 URHG Missbrauch von Künstlernamen",
    "§154 URHG Verstöße gegen das Verlagsrecht",
    "§155 URHG Verstöße gegen das Filmrecht",
    "§156 URHG Nutzung von urheberrechtlich geschützten Softwareprogrammen",
    "§157 URHG Missbrauch von Filmrechten",
    "§158 URHG Urheberrechtlicher Missbrauch im Internet",
    "§159 URHG Softwarepiraterie",
    "§160 URHG Verstöße gegen das Designrecht",
    "§161 URHG Verstöße gegen das Patentrecht",
    "§162 URHG Verstöße gegen das Markenrecht",
    "§163 UWG Unlautere Werbung",
    "§164 UWG Irreführende Werbung",
    "§165 UWG Unzulässige Preisabsprachen",
    "§166 UWG Missbrauch von Marktpositionen",
    "§167 UWG Wettbewerbswidriges Verhalten",
    "§168 UWG Missbrauch von sozialen Medien",
    "§169 UWG Verstöße gegen das Wettbewerbsrecht",
    "§170 UWG Verstöße gegen die Vorschriften zu Werbeanzeigen",
    "§171 UWG Verstöße gegen das Recht auf Werbung",
    "§172 UWG Wettbewerbsvorteil durch unlautere Werbung",
    "§173 UWG Unzulässige Absprachen zwischen Unternehmen",
    "§181 BDSG Unzulässige Überwachung von Mitarbeitern",
    "§182 BDSG Missbrauch von Daten durch Unternehmen",
    "§211 StGB Mord",
    "§212 StGB Totschlag",
    "§223 StGB Körperverletzung",
    "§224 StGB Gefährliche Körperverletzung",
    "§225 StGB Misshandlung von Schutzbefohlenen",
    "§229 StGB Fahrlässige Körperverletzung",
    "§243 StGB Besonders schwerer Diebstahl",
    "§244 StGB Diebstahl mit Waffen",
    "§247 StGB Unterschlagung",
    "§263 StGB Betrug",
    "§267 StGB Urkundenfälschung",
    "§272 StGB Diebstahl von Gebrauchsgütern",
    "§278 StGB Erpressung",
    "§286 StGB Verletzung von Geheimnissen",
    "§303 StGB Sachbeschädigung",
    "§304 StGB Graffiti",
    "§305 StGB Zerstörung von Kulturgütern",
    "§307 StGB Gefährdung durch Brandstiftung",
    "§323 StGB Notrufmissbrauch",
    "§324 StGB Störung des öffentlichen Friedens",
]

    return random.choice(gericht)