import com.univocity.parsers.csv.CsvParserSettings
import com.univocity.parsers.csv.CsvParser
import com.univocity.parsers.common.processor.BeanListProcessor
import com.univocity.parsers.csv.CsvWriterSettings
import com.univocity.parsers.csv.CsvWriter
import java.io.FileReader
import java.io.FileWriter

# Declare settings as CsvParserSettings
settings = CsvParserSettings()

# Set line separator in settings
settings.getFormat().setLineSeparator("\n")

# Declare rowProcessor as BeanListProcessor<Employee> with Employee class
rowProcessor = BeanListProcessor(Employee.class)

# Set rowProcessor in settings
settings.setProcessor(rowProcessor)

# Create parser as CsvParser with settings
parser = CsvParser(settings)

# Parse CSV file using FileReader("/examples/employees.csv") and store in resolvedBeans
resolvedBeans = parser.parseAll(FileReader("/examples/employees.csv"))

# Declare writerSettings as CsvWriterSettings
writerSettings = CsvWriterSettings()

# Create writerSettings with rowWriterProcessor as BeanWriterProcessor<Employee> with Employee class
writerSettings.setRowWriterProcessor(new BeanWriterProcessor<Employee>(Employee.class))

# Create writer as CsvWriter with FileWriter("/examples/processed_employees.csv") and writerSettings
writer = new CsvWriter(FileWriter("/examples/processed_employees.csv"), writerSettings)

# Process records in writer with resolvedBeans
writer.processRecords(resolvedBeans)

# Write rows in writer with empty ArrayList<List<Object>>
writer.writeRows(new ArrayList<List<Object>>())