package fitbit.simcomp;

import com.pygmalios.reactiveinflux.jawa.*;
import com.pygmalios.reactiveinflux.jawa.sync.JavaSyncReactiveInflux;
import com.pygmalios.reactiveinflux.jawa.sync.SyncReactiveInflux;
import com.pygmalios.reactiveinflux.jawa.sync.SyncReactiveInfluxDb;
import org.joda.time.DateTime;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

public class SimilarityCompute 
{
	private static final long awaitAtMostMillis = 30000;
    public static void main( String[] args )
    {
    	// Use Influx at the provided URL
        ReactiveInfluxConfig config = new JavaReactiveInfluxConfig(new URI("http://localhost:8086/"));
        try (SyncReactiveInflux reactiveInflux = new JavaSyncReactiveInflux(config, awaitAtMostMillis)) {
            // Use database "example1"
            SyncReactiveInfluxDb db = reactiveInflux.database("example1");
    }
}
