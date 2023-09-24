<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>

<html>
<head>
    <title>Login Page</title>
</head>
<body align="center" bgcolor="#ffffcc">
    <h1>Login Page</h1>
    <html:form action="/login">
        <table align="center">
            <tr>
                <td>Username:</td>
                <td><html:text property="username" /></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><html:password property="password" /></td>
            </tr>
            <tr><td></td>
                <td colspan="2">
                    <html:submit value="Login" />
                </td>
            </tr>
        </table>
    </html:form>
</body>
</html>
