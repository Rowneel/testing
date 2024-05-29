using Microsoft.EntityFrameworkCore;

namespace WebApplicationMVC.Models
{
    public class DataDbContext : DbContext
    {
        public DataDbContext(DbContextOptions options) : base(options)
        {

        }
        public DbSet<Book> Book { get; set; }
    }
}
