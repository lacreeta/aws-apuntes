from setuptools import setup, find_packages

setup(
    name='mkdocs-exam-checklist',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['mkdocs>=1.0'],
    entry_points={
        'mkdocs.plugins': [
            'exam_checklist = plugins.exam_checklist:ExamChecklistPlugin'
        ]
    }
)
