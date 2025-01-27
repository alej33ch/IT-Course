# Vorfall-Management Playbook 

## 1. Erkennung des Vorfalls
Wenn ein Vorfall von einem Mitarbeiter erkannt wird, muss folgendes Verfahren befolgt werden:

- **Sofortige Benachrichtigung** an das IT-Team.
- Details angeben, wie den Vorfalltyp, betroffene Systeme und mögliche "Symptome".

## 2. Analyse und Bestätigung
Das IT-Team führt eine erste Analyse durch, um die Schwere des Vorfalls zu bestimmen:

- Überprüfung von Logs.
- Identifizierung ungewöhnlicher Verhaltensweisen.
- Bestätigung der Art der Bedrohung (Malware, unbefugter Zugriff, etc.).

## 3. Eindämmung
Nachdem der Vorfall bestätigt wurde, werden folgende Maßnahmen ergriffen:

- **Trennen des betroffenen Systems** vom Netzwerk.
- **Blockierung des externen Zugriffs** auf das kompromittierte System.
- **Ändern von Passwörtern** für kritische Systeme.

## 4. Beseitigung
Nachdem der Vorfall eingedämmt wurde, arbeitet das IT-Team daran, die Bedrohung zu beseitigen:

- **Entfernen von Malware** oder unerlaubter Software.
- **Systeme aktualisieren**, um Schwachstellen zu schließen.
- **Desinfizieren** von betroffenen Geräten und Systemen.

## 5. Wiederherstellung
Ziel ist es, die normalen Systemfunktionen wiederherzustellen:

- **Wiederherstellung von Daten** aus sicheren Backups.
- **Durchführen von Validierungstests**, um sicherzustellen, dass die Systeme frei von Bedrohungen sind.
- **Wiederanbindung von Systemen** an das Netzwerk auf sichere Weise.

## 6. Nachbesprechung
Nachdem der Vorfall gelöst wurde, führt das Team eine Post-Mortem-Analyse durch:

- **Identifizierung der Ursachen** des Vorfalls.
- **Aktualisierung der Sicherheitsverfahren**.
- **Implementierung neuer Präventionsmassnahmen**, um zukünftige Vorfälle zu vermeiden.

---



# Vorfall-Management Prozess


```mermaid
%%{init: {"themeVariables": {"title": "Vorfallmanagement-Prozess"}}}%%
graph TD
    A[Erkennung des Vorfalls] -->|Benachrichtigung an IT| B(Analyse und Bestätigung)
    B --> C{Schwere des Vorfalls}
    C -->|Malware| D[Malware entfernen]
    C -->|Unbefugter Zugriff| E[Zugang blockieren]
    C -->|Sonstiges| F[Untersuchen]
    D --> G[Systeme aktualisieren]
    E --> H[Passwörter ändern]
    F --> I[Überprüfung auf Sicherheitslücken]
    G --> J[Desinfizieren von Geräten]
    H --> J
    I --> J
    J --> K[Wiederherstellung der Systeme]
    K --> L[Nachbesprechung]
