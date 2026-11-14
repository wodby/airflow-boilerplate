# Airflow boilerplate

Keep your Apache Airflow DAGs, plugins and Python packages in Git and deploy
them with Wodby.

Use it with the [Apache Airflow stack](https://github.com/wodby/stack-airflow),
whose [Airflow service](https://github.com/wodby/service-airflow) builds from
this repository.

## Airflow's version

Choose the Airflow version for the service when you create the app. The build
starts from the official `apache/airflow` image of that version and adds your
DAGs, plugins and packages. Every Airflow component, including the scheduler
and DAG processor, runs that image.

## DAGs and plugins

Put DAG files in `dags/` and plugins in `plugins/`. `dags/example.py` is an
example; replace it with your own.

## Python packages

List the packages your DAGs need, such as Airflow providers, in
`requirements.txt`. The build installs them with Airflow pinned to the image's
version, so a package that needs another Airflow version fails the build. Don't
list `apache-airflow` itself.

## Files

| Path | Purpose |
| --- | --- |
| `dags/` | Your DAGs |
| `plugins/` | Your Airflow plugins |
| `requirements.txt` | Python packages your DAGs need |
| `.wodby/pipeline.yml` | The Wodby CI pipeline that builds and deploys the image |
| `.dockerignore` | Files left out of the build |
