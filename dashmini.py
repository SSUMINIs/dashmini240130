# -*- coding:utf-8 -*-

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import plotly

#@st.cache_data
#data_ais = 'csv/aisles.csv/aisles.csv'
data_dep = 'csv/departments.csv/departments.csv'
#data_ord_pr = 'csv/order_products__prior.csv/order_products__prior.csv'
data_ord_pr1 = 'csv/order_prior_100.csv'
#data_ord_tr = 'csv/order_products__train.csv/order_products__train.csv'
#data_ords = 'csv/orders.csv/orders.csv'
data_pro = 'csv/products.csv'
#data_samp = 'csv/sample_submission.csv/sample_submission.csv'


def main():
    st.markdown("<h1 style='text-align: center; color: black;'>주문고객 대시보드<hr></h1>", unsafe_allow_html=True)
    
    #aisles = pd.read_csv(data_ais)
    departments = pd.read_csv(data_dep)
    #order_products_prior = pd.read_csv(data_ord_pr)
    order_products_prior1 = pd.read_csv(data_ord_pr1)
    #order_products_train = pd.read_csv(data_ord_tr)
    #orders = pd.read_csv(data_ords)
    products = pd.read_csv(data_pro)
    #sample_submission = pd.read_csv(data_samp)
    merged_df = pd.merge(order_products_prior1, products, on='product_id', how='left')
    merged_df1 = pd.merge(merged_df, departments, on='department_id', how='left')
    #st.write(aisles)
    #st.write(departments)
    #st.write(order_products_prior)
    #st.write(order_products_train)
    #st.write(orders)
    #st.write(products)
    #st.write(sample_submission)
    col1, col2 = st.columns(2)
    col1.header("재구매 주문수 비교")
    re = col1.radio("재구매여부", ("재구매","재구매없음"))
    #n_reorder = order_products_prior1.loc[order_products_prior1['reordered']== '0']
    #y_reorder = order_products_prior1.loc[order_products_prior1['reordered']== '1']
    #y_reorderf = px.scatter('y_reorder', x='order_id', y= 'product_id')
    #n_reorderf = px.scatter('n_reorder', x='order_id', y='product_id')
    counts = order_products_prior1['reordered'].value_counts()
    
    #counts_y = order_products_prior1.loc[order_products_prior1['reordered']== 1].value_counts()
    if re == "재구매":
        fig = px.bar(counts, x={0:'재구매x', 1:'재구매o'}, 
                     y=counts.values, labels={'x':'재구매여부', 'y':'주문수'}, 
                     color=['lightgrey', 'blue'], color_discrete_map="identity")
        col1.plotly_chart(fig)
    else:
        fig = px.bar(counts, x={0:'재구매x', 1:'재구매o'}, 
                     y=counts.values, labels={'x':'재구매여부', 'y':'주문수'}, 
                     color=['blue', 'lightgrey'], color_discrete_map="identity")
        col1.plotly_chart(fig)

    #st.title('Scatter Plot with Plotly')
    #fig = go.Figure(data=go.Bar(x = no_reorder['reordered']))
    #st.plotly_chart(fig)
    #if yn_reorder == '재구매':
        #fig = go.Figure(y_reorderf)
        #st.plotly_chart(fig)
    #else:
        #fig = go.Figure(n_reorderf)
        #st.plotly_chart(fig)
    col2.header("재구매 고객의 상품 종류 확인")
   
    y_dep = merged_df1.loc[merged_df1['reordered'] == 1]
    re2 = col2.selectbox("상품종류", (y_dep['department'].unique()))
    counts1 = y_dep['department'].value_counts()
    
    y_dep1 = px.bar(y_dep, x=y_dep['department'].unique(), y=counts1.values, labels={'x':'상품 종류', 'y':'주문수'})
    fig = go.Figure(y_dep1)
    col2.plotly_chart(fig)
    
if __name__ == "__main__":
    main()