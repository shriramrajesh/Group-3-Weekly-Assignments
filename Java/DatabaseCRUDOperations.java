import java.sql.*;
public class DatabaseCRUDOperations {
	public static void main(String[] args) {
		String Name = "David";
		int ID = 101;
		int Salary = 40000;
		int Department_ID = 1;
		String City = "Mumbai";
		try {
			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/database", "root", "Misc2020");
			PreparedStatement statement = con
					.prepareStatement("INSERT INTO employee (Name,ID,Salary,Department_id,City) VALUES (?, ?, ?, ?,?)");
			statement.setString(1, Name);
			statement.setInt(2, ID);
			statement.setInt(3, Salary);
			statement.setInt(4, Department_ID);
			statement.setString(5, City);
			int rows = statement.executeUpdate();
			if (rows > 0)
				System.out.println("Table inserted");
			Statement statement1 = con.createStatement();
			ResultSet rs = statement1.executeQuery("select * from EMPLOYEE");
			while (rs.next()) {
				Name = rs.getString("Name");
				ID = rs.getInt("ID");
				Salary = rs.getInt("Salary");
				Department_ID = rs.getInt("Department_ID");
				City = rs.getString("City");
				System.out.println(Name + "," + ID + "," + Salary + "," + Department_ID + "," + City);
			}
			City = "Bangalore";
			PreparedStatement statement2 = con.prepareStatement("update employee set City=?");
			statement2.setString(1, City);
			rows = statement2.executeUpdate();
			if (rows > 0)
				System.out.println("Updated");
			PreparedStatement statement3 = con.prepareStatement("delete from employee where City=?");
			statement3.setString(1, City);
			rows = statement3.executeUpdate();
			if (rows > 0)
				System.out.println("Deleted");
			con.close();
		} catch (SQLException ex) {
			ex.printStackTrace();
		}
	}
}
