FROM public.ecr.aws/lambda/python:3.8

COPY docker/db_migrator/db_migrator.py ${LAMBDA_TASK_ROOT}
COPY alembic.ini ${LAMBDA_TASK_ROOT}
COPY migrations ${LAMBDA_TASK_ROOT}/migrations
COPY layers/forms_api_common ${LAMBDA_TASK_ROOT}/forms_api_common
ENV PYTHONPATH "${PYTHONPATH}:${LAMBDA_TASK_ROOT}/forms_api_common"
COPY requirements.lock ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.lock
CMD ["db_migrator.handler"]
