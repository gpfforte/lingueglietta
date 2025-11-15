# Progetto Web Lingueglietta

Questo repository contiene il codice sorgente per il sito web di Lingueglietta, un'applicazione web basata su Django.

## Caratteristiche Principali

*   **Gestione Utenti**: Registrazione con conferma via email, login, cambio e reset password.
*   **Profili Utente**: Ogni utente ha un proprio profilo con la possibilità di caricare un'immagine personale.
*   **Sistema di Blog**: Creazione e visualizzazione di articoli (post).
*   **Commenti**: Gli utenti registrati possono commentare i post. Ogni utente può modificare o cancellare solo i propri commenti.
*   **Moderazione**: Solo i post e i commenti approvati (con flag `published` a `True`) sono visibili pubblicamente.
*   **Pagine Statiche**: Un'app dedicata (`info`) per la gestione di contenuti più statici ed editoriali.

## Stack Tecnologico

*   **Backend**: Django
*   **Database**: PostgreSQL
*   **Containerizzazione**: Docker e Docker Compose

---

## Ambiente di Sviluppo

L'ambiente di sviluppo è completamente containerizzato tramite Docker per garantire coerenza e facilità di setup. Non è necessario installare Python o PostgreSQL localmente, ma solo Docker.

### Prerequisiti

*   Docker
*   Docker Compose (solitamente incluso con Docker Desktop)

### Avvio dell'ambiente

1.  **Clona il repository**:
    ```bash
    git clone <URL_DEL_TUO_REPOSITORY>
    cd lingueglietta
    ```

2.  **Avvia i container**:
    Esegui il seguente comando dalla root del progetto per avviare i servizi (web app e database) in background:
    ```bash
    docker-compose up -d --build
    ```
    L'applicazione web sarà accessibile all'indirizzo http://localhost:8000.

3.  **Eseguire comandi Django**:
    Per eseguire comandi di Django come `migrate` o `createsuperuser`, utilizza `docker-compose exec`:
    ```bash
    # Esempio: applicare le migrazioni del database
    docker-compose exec web python manage.py migrate

    # Esempio: creare un superuser
    docker-compose exec web python manage.py createsuperuser
    ```

## Ambiente di Produzione

La configurazione per la produzione si trova in un altro progetto (`gpfblog`), che gestisce il deploy di tutti i servizi necessari tramite un unico file `docker-compose.prod.yml`.
