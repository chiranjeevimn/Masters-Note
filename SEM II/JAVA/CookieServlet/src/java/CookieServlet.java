import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CookieServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            String s1 = request.getParameter("special");
            String s2 = request.getParameter("pname");
            Cookie c1 = new Cookie("Specialization",s1);
            Cookie c2 = new Cookie("Person",s2);
            response.addCookie(c1);
            response.addCookie(c2);
            c1.setMaxAge(60);
            c2.setMaxAge(31536000);
            out.println("Cookie set for a minute");
           
        }
    }

}
