from celery.task import task
from statsmodels.robust import mad


@task
def task_mad(data):
    """
    http://statsmodels.sourceforge.net/devel/generated/statsmodels.robust.scale.mad.html
    """

    mad_value = mad(data)

    return mad_value
