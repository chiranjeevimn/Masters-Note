
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class readCookie extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            Cookie cookie = null;
            Cookie[] cookies = null;
            cookies = request.getCookies();
            String title = "Reading Cookies Example";
            if (cookies != null) {
                out.println("Found Cookies Name and Value");
                for (int i = 0; i < cookies.length; i++) {
                    cookie = cookies[i];
                    out.println("Specialization : " + cookie.getName() + ",");
                    out.println("Value: " + cookie.getValue() + " ");
                }
            } else {
                out.println("No cookies found");

            }
        }

    }
}
