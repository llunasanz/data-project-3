import pandas as pd
import datetime as dt
import sweetviz as sv
import datetime as dt

# Get URLs
url_test_prev = 'https://raw.githubusercontent.com/llunasanz/data-project-3/main/raw_data/test_previous_loan.csv'
url_train_prev = 'https://raw.githubusercontent.com/llunasanz/data-project-3/main/raw_data/train_previous_loan.csv'

url_test_perf = 'https://raw.githubusercontent.com/llunasanz/data-project-3/main/raw_data/test_performance.csv'
url_train_perf = 'https://raw.githubusercontent.com/llunasanz/data-project-3/main/raw_data/train_performance.csv'

url_test_demo = 'https://raw.githubusercontent.com/llunasanz/data-project-3/main/raw_data/test_datos_demograficos.csv'
url_train_demo = 'https://raw.githubusercontent.com/llunasanz/data-project-3/main/raw_data/train_datos_demograficos.csv'


# Read files
df_tr_demo = pd.read_csv(url_train_demo)
df_ts_demo = pd.read_csv(url_test_demo)

df_tr_previous = pd.read_csv(url_train_prev)
df_ts_previous = pd.read_csv(url_test_prev)

df_tr_performance = pd.read_csv(url_train_perf)
df_ts_performance = pd.read_csv(url_test_perf)


# Concatenate
df_demo = pd.concat([df_tr_demo, df_ts_demo], axis = 0)
df_previous = pd.concat([df_tr_previous, df_ts_previous], axis = 0)
df_performance = pd.concat([df_tr_performance, df_ts_performance], axis = 0)


# Modify data
df_demo.birthdate = pd.to_datetime(df_demo.birthdate)

df_previous.approveddate = pd.to_datetime(df_previous.approveddate)
df_previous.creationdate = pd.to_datetime(df_previous.creationdate)
df_previous.closeddate = pd.to_datetime(df_previous.closeddate)
df_previous.firstduedate = pd.to_datetime(df_previous.firstduedate)
df_previous.firstrepaiddate = pd.to_datetime(df_previous.firstrepaiddate)

df_tr_performance.approveddate = pd.to_datetime(df_tr_performance.approveddate)
df_tr_performance.creationdate = pd.to_datetime(df_tr_performance.creationdate)
df_ts_performance.approveddate = pd.to_datetime(df_tr_performance.approveddate)
df_ts_performance.creationdate = pd.to_datetime(df_tr_performance.creationdate)
df_performance.approveddate = pd.to_datetime(df_tr_performance.approveddate)
df_performance.creationdate = pd.to_datetime(df_tr_performance.creationdate)


sweet_report = sv.analyze(df_demo)
sweet_report.show_html('demographic_data_report.html')
sweet_report = sv.analyze(df_previous)
sweet_report.show_html('previous_data_report.html')
sweet_report = sv.analyze(df_performance)
sweet_report.show_html('performance_data_report.html')
sweet_report = sv.analyze(df_tr_performance)
sweet_report.show_html('train_performance_data_report.html')
sweet_report = sv.analyze(df_ts_performance)
sweet_report.show_html('test_performance_data_report.html')
