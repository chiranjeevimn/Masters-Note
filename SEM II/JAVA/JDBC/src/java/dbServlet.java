import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class dbServlet extends HttpServlet {
private Connection con = null;
private Statement st = null;
private final ResultSet rs = null;
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            con = DriverManager.getConnection("jdbc:derby://localhost:1527/mydb","mydb","mydb");
            
            String s1 = request.getParameter("name");
            String s2 = request.getParameter("contact");
            String s3 = request.getParameter("email");
            out.println("Verify your credentials");
            out.println("Your name is :"+s1+"<br/>");
            out.println("Your contact is :"+s2+"<br/>");
            out.println("Your Email is :"+s3+"<br/>");
            String ch = request.getParameter("choice");
            switch(ch)
            {
                case"Insert":
                    String qry = "insert into register values('"+s1+"','"+s2+"','"+s3+"')";
                    st = con.createStatement();
                    int r = st.executeUpdate(qry);
                    out.println(r +"inserted");
                    break;
                case"Delete": 
                    String q1 = " delete from register where name='"+s1+"'";
                    st = con.createStatement();
                    st.execute(q1);
                    out.println("  deleted");
                    break;
                case"Update": break;
                case"Showall": break;
                default: break;
            }
        } catch (ClassNotFoundException | SQLException ex) {
        Logger.getLogger(dbServlet.class.getName()).log(Level.SEVERE, null, ex);
    }
    }
}
