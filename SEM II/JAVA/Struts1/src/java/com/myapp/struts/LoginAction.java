package com.myapp.struts;

import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionForward;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LoginAction extends Action {
    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form,
            HttpServletRequest request, HttpServletResponse response)
            throws Exception {
        // Add your login logic here
        String username = ((LoginForm) form).getUsername();
        String password = ((LoginForm) form).getPassword();

        // For simplicity, check if username and password are "admin"
        if ("Chiru".equals(username) && "admin".equals(password)) {
            return mapping.findForward("success"); // Forward to a success page
        } else {
            return mapping.findForward("failure"); // Forward to a failure page
        }
    }
}
